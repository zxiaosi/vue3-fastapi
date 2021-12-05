<template>
  <div>
    <header-name :iconName='state.iconName' :pageName='state.pageName' />

    <!-- 表格 -->
    <div class="container">
      <!-- 排序和添加 -->
      <header-handle :query="query" :data="state.courseData" :formData="formData"
        :isShowSearched="state.isShowSearched" :selectedList="state.selectedList"
        :read_datas="read_courses" :delete_data="delete_course" :removeSearch="removeSearch"
        @searchedData='searchedData' @isAddDialog='isAddDialog' />

      <!-- 表格信息 -->
      <el-table
        :data="state.isShowSearched 
                ? state.searched 
                : state.courseData.slice((query.currentPage-1)*(query.pageSize),(query.currentPage)*(query.pageSize))"
        border stripe class="table" max-height="578"
        :default-sort="{ prop: 'id', order: 'ascending' }"
        @selection-change="handleSelectionChange">

        <!-- 勾选框 -->
        <el-table-column type="selection" width="80" align="center" />

        <!-- 序号 -->
        <el-table-column label="序号" type="index" width="80" align="center" fixed />

        <el-table-column prop="id" label="课程编号" width="140" align="center" sortable
          :sort-orders="['ascending', 'descending']" />
        <el-table-column prop="name" label="课程名字" width="220" align="center" />
        <el-table-column prop="credit" label="学分" width="140" align="center" />
        <el-table-column prop="period" label="课时" min-width="140" align="center" />

        <!-- 操作 -->
        <handle :data="state.courseData" :formData="formData" :delete_data="delete_course"
          :removeSearch="removeSearch" @isAddDialog='isAddDialog' @subIndexId='subIndexId' />
      </el-table>

      <!-- 页码 -->
      <pagination :pageSize="query.pageSize" :pageTotal="state.pageTotal"
        :currentPage="query.currentPage" :render='getData' @pageIndex='pageIndex' />
    </div>

    <!-- 编辑弹出框 -->
    <el-dialog :title="`${state.addOrUpdate ? '添加课程信息' : '编辑课程信息'}`" v-model="state.showDialog"
      width="30%">

      <el-form status-icon label-width="100px" ref="formRef" :model="formData" :rules="formRules"
        autocomplete="on">
        <el-form-item label="课程编号" prop="id">
          <el-input v-model="formData.id" placeholder="编号" maxlength="4"
            :disabled=!state.addOrUpdate />
        </el-form-item>
        <el-form-item label="课程名字" prop="name">
          <el-input v-model="formData.name" placeholder="名字" maxlength="20" />
        </el-form-item>
        <el-form-item label="学分" prop="credit">
          <el-input v-model="formData.credit" placeholder="学分" maxlength="2" />
        </el-form-item>
        <el-form-item label="课时" prop="period">
          <el-input v-model="formData.period" placeholder="课时" maxlength="2" />
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
  read_courses,
  create_course,
  update_course,
  delete_course,
} from '../../api/course';

// 变量
const state = reactive({
  iconName: 'cascades', // 页面icon名字
  pageName: '课程表', // 页面名字
  courseData: [], // 课程表数据
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
  read_courses()
    .then((res) => {
      state.courseData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载课程信息数据失败');
    });
}

// 页面加载后调用函数
onMounted(() => {
  getData();
});

// 监听属性
watchEffect(() => {
  state.pageTotal = state.courseData.length || query.pageSize;
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
  credit: '',
  period: '',
});

// 定义校验规则
const formRules = reactive({
  id: [
    {
      required: 'true',
      pattern: /^[1-9]/,
      message: '请输入课程编号(以1-9开头)',
      trigger: 'change',
    },
    { min: 4, message: '课程编号的长度应为4' },
  ],
  name: [
    {
      required: 'true',
      message: '请输入课程名称',
      trigger: ['change', 'blur'],
    },
  ],
  credit: [
    { required: 'true', message: '请输入学时', trigger: ['change', 'blur'] },
  ],
  period: [
    { required: 'true', message: '请输入学分', trigger: ['change', 'blur'] },
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
      create_course(formData)
        .then((res) => {
          if (res.code == 200) {
            state.courseData.push(res.data);
            ElMessage.success(`成功添加编号为${res.data.id}的课程信息！`);
          } else {
            ElMessage.warning('院系信息填写有误，添加失败！');
          }
        })
        .catch(() => {
          ElMessage.error('添加课程信息失败！');
        });
    } else {
      ElMessage.warning('课程信息不符合校验规则，添加失败！');
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
      update_course(idx, formData)
        .then((res) => {
          ElMessage.success(`修改课程ID为 ${idx} 成功！`);
          Object.keys(res.data).forEach((item) => {
            state.courseData[reIndex][item] = res.data[item];
          });
          state.searched[0] = formData;
          getData();
        })
        .catch(() => {
          ElMessage.error('修改课程信息失败！');
        });
    } else {
      ElMessage.warning('填写课程不符合校验规则，修改失败！');
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