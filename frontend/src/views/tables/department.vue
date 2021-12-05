<template>
  <div>
    <header-name :iconName='state.iconName' :pageName='state.pageName' />

    <!-- 表格 -->
    <div class="container">

      <!-- 搜索和添加 -->
      <header-handle :query="query" :data="state.deptData" :formData="formData"
        :isShowSearched="state.isShowSearched" :selectedList="state.selectedList"
        :read_datas="read_departments" :delete_data="delete_department" :removeSearch="removeSearch"
        @searchedData='searchedData' @isAddDialog='isAddDialog' />

      <!-- 表格信息 -->
      <el-table
        :data="state.isShowSearched 
                ? state.searched 
                : state.deptData.slice((query.currentPage-1)*(query.pageSize),(query.currentPage)*(query.pageSize))"
        border stripe class="table" max-height="578"
        :default-sort="{ prop: 'id', order: 'ascending' }"
        @selection-change="handleSelectionChange">

        <!-- 勾选框 -->
        <el-table-column type="selection" width="80" align="center" />

        <!-- 序号 -->
        <el-table-column label="序号" type="index" width="80" align="center" fixed />

        <el-table-column prop="id" label="院系编号" width="140" align="center" sortable
          :sort-orders="['ascending', 'descending']" />
        <el-table-column prop="name" label="院系名字" width="220" align="center" />
        <el-table-column prop="chairman" label="主任名" width="140" align="center" />
        <el-table-column prop="phone" label="主任手机号" min-width="180" align="center" />

        <!-- 操作 -->
        <handle :data="state.deptData" :formData="formData" :delete_data="delete_department"
          :removeSearch="removeSearch" @isAddDialog='isAddDialog' @subIndexId='subIndexId' />
      </el-table>

      <!-- 页码 -->
      <pagination :pageSize="query.pageSize" :pageTotal="state.pageTotal"
        :currentPage="query.currentPage" :render='getData' @pageIndex='pageIndex' />
    </div>

    <!-- 编辑弹出框 -->
    <el-dialog :title="`${state.addOrUpdate ? '添加院系信息' : '编辑院系信息'}`" v-model="state.showDialog"
      width="30%">

      <el-form status-icon label-width="100px" ref="formRef" :model="formData" :rules="formRules"
        autocomplete="on">
        <el-form-item label="院系编号" prop="id">
          <el-input v-model="formData.id" placeholder="编号" maxlength="4"
            :disabled=!state.addOrUpdate />
        </el-form-item>
        <el-form-item label="院系名字" prop="name">
          <el-input v-model="formData.name" placeholder="名字" maxlength="20" />
        </el-form-item>
        <el-form-item label="主任名" prop="chairman">
          <el-input v-model="formData.chairman" placeholder="主任名" maxlength="10" />
        </el-form-item>
        <el-form-item label="主任手机号" prop="phone">
          <el-input v-model="formData.phone" type="tel" placeholder="手机号" maxlength="11" />
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
  read_departments,
  create_department,
  update_department,
  delete_department,
} from '../../api/department';

// 变量
const state = reactive({
  iconName: 'cascades', // 页面icon名字
  pageName: '院系表', // 页面名字
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
  currentPage: 1, // 当前页
  pageSize: 10, // 每页多少
});

let idx = -1; // 临时编号
let reIndex = -1; // 临时序号

/**
 * 获取表格数据
 */
const getData = () => {
  read_departments()
    .then((res) => {
      state.deptData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载院系信息数据失败!');
    });
};

// 页面加载后调用函数
onMounted(() => {
  getData();
});

// 监听属性
watchEffect(() => {
  state.pageTotal = state.deptData.length || query.pageSize;
});

/**
 * 当前页码(子组件传递的值)
 */
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
  chairman: '',
  phone: '',
});

// 定义校验规则
const formRules = reactive({
  id: [
    { required: 'true', trigger: 'change', message: '请输入院系编号' },
    { pattern: /^10/, message: '请输入院系编号(以10开头)' },
    { pattern: /^10[0-9]{2}/, message: '院系编号为四位整数' },
    { min: 4, max: 4, message: '院系编号的长度应为4' },
  ],
  name: [
    {
      required: 'true',
      message: '请输入院系名称(最大长度为20)',
      trigger: ['change', 'blur'],
    },
  ],
  chairman: [
    {
      required: 'true',
      message: '请输入院系主任名(最大长度为10)',
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
      create_department(formData)
        .then((res) => {
          if (res.code == 200) {
            state.deptData.push(res.data);
            ElMessage.success(`成功添加编号为${res.data.id}的院系信息！`);
            removeSearch();
          } else {
            ElMessage.warning('院系信息填写有误，添加失败！');
          }
        })
        .catch(() => {
          ElMessage.error('添加院系信息失败！');
        });
    } else {
      ElMessage.warning('院系信息不符合校验规则，添加失败！');
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
  state.showDialog = state.addOrUpdate = false;

  formRef.value.validate((valid) => {
    if (valid) {
      update_department(idx, formData)
        .then((res) => {
          ElMessage.success(`修改院系ID为 ${idx} 成功！`);
          Object.keys(res.data).forEach((item) => {
            state.deptData[reIndex][item] = res.data[item];
          });
          state.searched[0] = formData;
          getData();
        })
        .catch(() => {
          ElMessage.error('修改院系信息失败！');
        });
    } else {
      ElMessage.warning('填写院系不符合校验规则，修改失败！');
    }
  });
}

/**
 * 清除搜索
 */
function removeSearch() {
  query.id = '';
  state.isShowSearched = false;
  getData();
}

// 可以省略
defineExpose({
  state,
  query,
  getData,
  pageIndex,
  searchedData,
  handleSelectionChange,
  formData,
  formRules,
  isAddDialog,
  saveAdd,
  subIndexId,
  saveEdit,
});
</script>

<style scoped>
.table {
  width: 100%;
  font-size: 14px;
  max-height: 578px;
}

.table-td-thumb {
  display: block;
  margin: auto;
  width: 40px;
  height: 40px;
}
</style>