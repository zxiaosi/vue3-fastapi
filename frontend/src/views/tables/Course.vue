<template>
  <base-table :page="page" :query="query" :data="state.courseData" :page-total="state.pageTotal" :form-data="formData"
    :form-rules="formRules" :get-data="getData" :apis="course_apis" @emit-is-disabled="emitIsDisabled"
    @emit-is-show-searched="emitIsShowSearched">

    <!-- 暂无 -->
    <template #filter />

    <!-- 渲染表格数据 -->
    <template #tableColumn>
      <el-table-column prop="id" label="课程编号" width="140" align="center" :sortable="!state.isShowSearched"
        :sort-orders="['ascending', 'descending']" />
      <el-table-column prop="name" label="课程名字" width="220" align="center" />
      <el-table-column prop="credit" label="学分" width="140" align="center" />
      <el-table-column prop="period" label="课时" min-width="140" align="center" />
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="课程编号" prop="id">
        <el-input v-model="formData.id" placeholder="请输入编号" maxlength="4" show-word-limit :disabled=state.isDisabled />
      </el-form-item>
      <el-form-item label="课程名字" prop="name">
        <el-input v-model="formData.name" placeholder="请输入名字" maxlength="20" show-word-limit />
      </el-form-item>
      <el-form-item label="学分" prop="credit">
        <el-input v-model="formData.credit" placeholder="请输入学分" maxlength="1" show-word-limit />
      </el-form-item>
      <el-form-item label="课时" prop="period">
        <el-input v-model="formData.period" placeholder="请输入课时" maxlength="2" show-word-limit />
      </el-form-item>
    </template>

  </base-table>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import { useStore } from 'vuex';
import { ElMessage } from 'element-plus';
import BaseTable from '@components/BaseTable.vue';
import course_apis from '@api/course';
import { byIdGetName } from '@utils/byIdGetName';

// 页面配置
const page = reactive({
  iconName: 'cascades', // 页面icon名字
  pageName: '课程', // 页面名字
  pageNameEn: 'course', // 页面英文名
});

// 变量
const state = reactive({
  courseData: [], // 课程表数据
  pageTotal: 0, // 数据的总个数
  isDisabled: false, // 是否禁用编辑框id
  isShowSearched: false, // 是否显示被搜索的
});

// 搜索和页码
const query = reactive({
  id: '',
  currentPage: 1,
  pageSize: 10,
});

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
    { required: 'true', trigger: 'change', message: '请输入课程编号' },
    { pattern: /^[1-9]/, message: '课程编号不能以0开头' },
    { min: 4, max: 4, message: '课程编号的长度应为4' },
    { pattern: /^[1-9][0-9]{3}$/, message: '课程编号必须是正整数' },
    { validator: checkId },
  ],
  name: [
    {
      required: 'true',
      message: '请输入课程名称',
      trigger: ['change', 'blur'],
    },
  ],
  credit: [
    { required: 'true', message: '请输入学分', trigger: ['change', 'blur'] },
    { pattern: /^[1-4]$/, message: '学分应在1-4之间' },
  ],
  period: [
    { required: 'true', message: '请输入课时', trigger: ['change', 'blur'] },
    {
      pattern: /^[1-9]$|^([1-2][0-9])$|^3[0-2]$/,
      message: '学时应在1-32之间',
    },
  ],
});

// 状态管理
const store = useStore();

/**
 * 获取表格数据
 */
async function getData(currentPage = 1) {
  // 获取课程表数据
  let params = { pageIndex: currentPage, pageSize: query.pageSize };
  const { data } = await course_apis.read_datas(params);
  state.courseData = data.dataList;
  state.pageTotal = data.count;
}

// 页面加载后调用函数
onMounted(() => {
  getData();
});

/**
 * 检查id是否存在(验证规则)
 */
function checkId(rule, value, callback) {
  if (state.isDisabled) {
    callback(); // 验证通过
  } else {
    if (
      state.courseData
        .map((item) => {
          return item.id;
        })
        .indexOf(value) != -1
    ) {
      callback(new Error('院系编号已经存在'));
    } else {
      callback(); // 验证通过
    }
  }
}

/**
 * 是否禁用编辑框id(子组件传值)
 */
function emitIsDisabled(res) {
  state.isDisabled = res;
}

/**
 * 是否显示被搜索的(子组件传值)
 */
function emitIsShowSearched(res) {
  state.isShowSearched = res;
}

/**
 * 获取下拉框的值
 */
function getChange(res) {
  console.log('下拉框的值为--', res);
}
</script>

<style scoped>
/* 选中框长度 */
.el-form-item .el-select {
  width: 100%;
}
</style>