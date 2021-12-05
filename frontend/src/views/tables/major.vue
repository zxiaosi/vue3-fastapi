<template>
  <div>
    <header-name :iconName='state.iconName' :pageName='state.pageName' />

    <!-- 表格 -->
    <div class="container">

      <!-- 搜索和添加 -->
      <header-handle :query="query" :data="state.majorData" :formData="formData"
        :isShowSearched="state.isShowSearched" :selectedList="state.selectedList"
        :read_datas="read_majors" :delete_data="delete_major" :removeSearch="removeSearch"
        @searchedData='searchedData' @isAddDialog='isAddDialog' />

      <!-- 表格信息 -->
      <el-table
        :data="state.isShowSearched 
                ? state.searched 
                : state.majorData.slice((query.currentPage-1)*(query.pageSize),(query.currentPage)*(query.pageSize))"
        border stripe class="table" max-height="578"
        :default-sort="{ prop: 'id', order: 'ascending' }"
        @selection-change="handleSelectionChange">

        <!-- 勾选框 -->
        <el-table-column type="selection" width="80" align="center" />

        <!-- 序号 -->
        <el-table-column label="序号" type="index" width="80" align="center" fixed />

        <el-table-column prop="id" label="专业编号" width="140" align="center" sortable
          :sort-orders="['ascending', 'descending']" />
        <el-table-column prop="name" label="专业名字" width="220" align="center" />
        <el-table-column prop="assistant" label="辅导员姓名" width="140" align="center" />
        <el-table-column prop="phone" label="辅导员手机号" width="180" align="center" />
        <el-table-column prop="department_name" label="院系名字" min-width="220" align="center" />

        <!-- 操作 -->
        <handle :data="state.majorData" :formData="formData" :delete_data="delete_major"
          :removeSearch="removeSearch" @isAddDialog='isAddDialog' @subIndexId='subIndexId' />
      </el-table>

      <!-- 页码 -->
      <pagination :pageSize="query.pageSize" :pageTotal="state.pageTotal"
        :currentPage="query.currentPage" :render='getData' @pageIndex='pageIndex' />
    </div>

    <!-- 编辑弹出框 -->
    <el-dialog :title="`${state.addOrUpdate ? '添加专业信息' : '编辑专业信息'}`" v-model="state.showDialog"
      width="30%">

      <el-form status-icon label-width="100px" ref="formRef" :model="formData" :rules="formRules"
        autocomplete="on">
        <el-form-item label="专业编号" prop="id">
          <el-input v-model="formData.id" placeholder="编号" maxlength="6"
            :disabled=!state.addOrUpdate />
        </el-form-item>
        <el-form-item label="专业名字" prop="name">
          <el-input v-model="formData.name" placeholder="名字" maxlength="20" />
        </el-form-item>
        <el-form-item label="辅导员姓名" prop="assistant">
          <el-input v-model="formData.assistant" placeholder="辅导员姓名" maxlength="10" />
        </el-form-item>
        <el-form-item label="辅导员手机号" prop="phone">
          <el-input v-model="formData.phone" placeholder="辅导员手机号" maxlength="11" />
        </el-form-item>
        <el-form-item label="院系名字" prop="department_id">
          <el-select v-model="formData.department_id" placeholder="请选择院系"
            @change="getChange(formData.department_id)">
            <el-option v-for="(dept, index) in state.deptData" :key=index :label=dept.name
              :value=dept.id />
          </el-select>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="state.showDialog = false">取 消</el-button>
          <el-button type="primary" v-if="state.addOrUpdate" @click="saveAdd">添 加</el-button>
          <el-button type="primary" v-else @click="saveEdit">更 新</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, watchEffect } from 'vue';
import { ElMessage } from 'element-plus';
import HeaderName from '../../components/tables/HeaderName.vue';
import HeaderHandle from '../../components/tables/HeaderHandle.vue';
import Handle from '../../components/tables/Handle.vue';
import Pagination from '../../components/tables/Pagination.vue';
import {
  read_majors,
  create_major,
  update_major,
  delete_major,
} from '../../api/major';
import { read_departments } from '../../api/department';

// 变量
const state = reactive({
  iconName: 'cascades', // 页面icon名字
  pageName: '专业表', // 页面名字
  majorData: [], // 专业表数据
  deptData: [], // 院系表数据
  pageTotal: 0, // 总个数
  isShowSearched: false, // 是否显示被搜索的
  searched: [], // 被搜索的数据(渲染表格数据需要是列表)
  selectedList: [], // 被勾选的的值
  showDialog: false, // 是否显示弹窗
  addOrUpdate: true, // 是否是添加或更新(true-添加 | false-更新)
});

// 搜索和页码
const query = reactive({
  id: '',
  currentPage: 1,
  pageSize: 10,
});

let idx = -1; // 临时编号
let reIndex = -1; // 临时序号

/**
 * 获取表格数据
 */
function getData() {
  read_majors()
    .then((res) => {
      state.majorData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载专业信息数据失败！');
    });

  // 获取院系信息
  read_departments()
    .then((res) => {
      state.deptData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载院系信息数据失败！');
    });
}

// 页面加载后调用函数
onMounted(() => {
  getData();
});

// 监听属性
watchEffect(() => {
  state.pageTotal = state.majorData.length || query.pageSize;
});

// 当前页码
function pageIndex(res) {
  query.currentPage = res;
}

/**
 * 显示被搜索的数据(子组件传值)
 */
function searchedData(res) {
  state.isShowSearched = true;
  state.searched.splice(0, 1, res);
}

/**
 * 被勾选的数据
 */
function handleSelectionChange(val) {
  if (val.length == 0) {
    state.selectedList = [];
  }

  val.forEach((item, index) => {
    state.selectedList.splice(index, 1, { reIndex: index, idx: item.id });
  });
}

// 校验规则
const formRef = ref();

// 表单对象
const formData = reactive({
  id: '',
  name: '',
  assistant: '',
  phone: '',
  department_id: '',
});

// 定义校验规则
const formRules = reactive({
  id: [
    {
      required: 'true',
      pattern: /^10[0-9]{2}/,
      message: '请输入专业编号(以10开头)',
      trigger: 'change',
    },
    { min: 6, message: '专业编号的长度应为6' },
  ],
  name: [
    {
      required: 'true',
      message: '请输入专业名称(最大长度为20)',
      trigger: ['change', 'blur'],
    },
  ],
  assistant: [
    {
      required: 'true',
      message: '请输入辅导员姓名(最大长度为10)',
      trigger: ['change', 'blur'],
    },
  ],
  phone: [
    {
      pattern: /^((0\d{2,3}-\d{7,8})|(1[34578]\d{9}))$/,
      message: '请输入正确的手机号',
      trigger: ['change', 'blur'],
    },
  ],
  department_id: [
    { required: 'true', message: '请选择院系', trigger: ['change'] },
  ],
});

/**
 * 添加、编辑表格的弹窗(子组件传递的值)
 */
function isAddDialog(show, addUpdate) {
  state.showDialog = show;
  state.addOrUpdate = addUpdate;
}

/**
 * 确认添加
 */
function saveAdd() {
  state.showDialog = false;

  formRef.value.validate((valid) => {
    if (valid) {
      create_major(formData)
        .then((res) => {
          if (res.code == 200) {
            state.majorData.push(res.data);
            ElMessage.success(`成功添加编号为${res.data.id}的专业信息！`);
            removeSearch();
          } else {
            ElMessage.warning('专业信息填写有误，添加失败！');
          }
        })
        .catch(() => {
          ElMessage.error('添加专业信息失败！');
        });
    } else {
      ElMessage.warning('专业信息不符合校验规则，添加失败！');
    }

    // 重置表单
    formRef.value.resetFields();
  });
}

/**
 * 获取索引和编号
 */
function subIndexId(index, id) {
  reIndex = index;
  idx = id;
}

/**
 * 确认更新
 */
function saveEdit() {
  state.addOrUpdate = state.showDialog = false;

  console.log(idx);

  formRef.value.validate((valid) => {
    if (valid) {
      update_major(idx, formData)
        .then((res) => {
          console.log(res);
          ElMessage.success(`修改专业ID为 ${idx} 成功！`);
          Object.keys(res.data).forEach((item) => {
            state.majorData[reIndex][item] = res.data[item];
          });
          state.searched[0] = formData;
          getData();
        })
        .catch(() => {
          ElMessage.error('修改专业信息失败！');
        });
    } else {
      ElMessage.warning('填写专业不符合校验规则，修改失败！');
    }
  });
}

/**
 * 获取多选框的值
 */
function getChange(value) {
  console.log(value);
}

/**
 * 清除搜索
 */
function removeSearch() {
  query.id = '';
  state.isShowSearched = false;
  getData();
}
</script>

<style scoped>
/* 选中框长度 */
.el-form-item .el-select {
  width: 100%;
}
.table {
  width: 100%;
  font-size: 14px;
}
.table-td-thumb {
  display: block;
  margin: auto;
  width: 40px;
  height: 40px;
}
</style>