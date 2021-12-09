<template>
  <base-table :page="page" :query="query" :data="state.deptData" :form="form" :get-data="getData"
    :apis="department_apis" @emit-is-disabled="emitIsDisabled"
    @emit-is-show-searched="emitIsShowSearched">

    <!-- 暂无 -->
    <template #filter />

    <!-- 渲染表格数据 -->
    <template #tableColumn>
      <el-table-column prop="id" label="院系编号" width="140" align="center"
        :sortable="!state.isShowSearched" :sort-orders="['ascending', 'descending']" />
      <el-table-column prop="name" label="院系名字" width="220" align="center" />
      <el-table-column prop="chairman" label="主任名" width="140" align="center" />
      <el-table-column prop="phone" label="主任手机号" min-width="180" align="center" />
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="院系编号" prop="id">
        <el-input v-model="form.data.id" placeholder="编号" maxlength="4"
          show-word-limit :disabled=state.isDisabled />
      </el-form-item>
      <el-form-item label="院系名字" prop="name">
        <el-input v-model="form.data.name" placeholder="名字" maxlength="20" />
      </el-form-item>
      <el-form-item label="主任名" prop="chairman">
        <el-input v-model="form.data.chairman" placeholder="主任名" maxlength="10" />
      </el-form-item>
      <el-form-item label="主任手机号" prop="phone">
        <el-input v-model="form.data.phone" type="tel" placeholder="手机号" maxlength="11" />
      </el-form-item>
    </template>

  </base-table>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import { ElMessage } from 'element-plus';
import BaseTable from '@components/BaseTable.vue';
import department_apis from '@api/department';

// 页面配置
const page = reactive({
  iconName: 'cascades', // 页面icon名字
  pageName: '院系', // 页面名字
});

// 变量
const state = reactive({
  deptData: [], // 院系表数据
  isDisabled: false, // 是否禁用编辑框id
  isShowSearched: false, // 是否显示被搜索的
});

// 搜索和页码
const query = reactive({
  id: '',
  currentPage: 1, // 当前页
  pageSize: 10, // 每页个数
});

// 表单信息
const form = reactive({
  // 表单对象
  data: {
    id: '',
    name: '',
    chairman: '',
    phone: '',
  },
  // 定义校验规则
  rules: {
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
  },
});

/**
 * 获取表格数据
 */
function getData() {
  department_apis
    .read_datas()
    .then((res) => {
      state.deptData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载院系信息数据失败!');
    });
}

// 页面加载后调用函数
onMounted(() => {
  getData();
});

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

// 可以省略
defineExpose({
  page,
  state,
  query,
  form,
  getData,
  emitIsDisabled,
  emitIsShowSearched,
});
</script>

<style scoped>
</style>