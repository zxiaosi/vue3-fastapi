<template>
  <base-table :page="page" :query="query" :data="state.majorData" :page-total="state.pageTotal" :form-data="formData"
    :form-rules="formRules" :get-data="getData" :apis="major_apis" @emit-is-disabled="emitIsDisabled"
    @emit-is-show-searched="emitIsShowSearched">
    <!-- 暂无 -->
    <template #filter />

    <!-- 渲染表格数据 -->
    <template #tableColumn>
      <el-table-column prop="id" label="专业编号" width="140" align="center" :sortable="!state.isShowSearched"
        :sort-orders="['ascending', 'descending']" />
      <el-table-column prop="name" label="专业名字" width="220" align="center" />
      <el-table-column prop="assistant" label="辅导员姓名" width="140" align="center" />
      <el-table-column prop="phone" label="辅导员手机号" width="180" align="center" />
      <el-table-column prop="department_id" label="院系名字" min-width="220" align="center">
        <template #default="scope">{{ byIdGetName(scope.row.department_id, state.deptData) }}</template>
      </el-table-column>
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="专业编号" prop="id">
        <el-input v-model="formData.id" placeholder="请输入编号" maxlength="6" show-word-limit
          :disabled="state.isDisabled" />
      </el-form-item>
      <el-form-item label="专业名字" prop="name">
        <el-input v-model="formData.name" placeholder="请输入名字" maxlength="20" show-word-limit />
      </el-form-item>
      <el-form-item label="辅导员姓名" prop="assistant">
        <el-input v-model="formData.assistant" placeholder="请输入辅导员姓名" maxlength="10" show-word-limit />
      </el-form-item>
      <el-form-item label="辅导员手机号" prop="phone">
        <el-input v-model="formData.phone" type="tel" placeholder="请输入辅导员手机号" maxlength="11" />
      </el-form-item>
      <el-form-item label="院系名字" prop="department_id">
        <el-select v-model="formData.department_id" placeholder="请选择院系" @change="getChange(formData.department_id)">
          <el-option v-for="(dept, index) in state.deptData" :key="index" :label="dept.name" :value="dept.id" />
        </el-select>
      </el-form-item>
    </template>
  </base-table>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import { useStore } from 'vuex';
import { ElMessage } from 'element-plus';
import BaseTable from '@components/BaseTable.vue';
import major_apis from '@api/major';
import department_apis from '@api/department';
import { byIdGetName } from '@utils/byIdGetName';
import { storeData } from '@utils/storeData';

// 页面配置
const page = reactive({
  iconName: 'cascades', // 页面icon名字
  pageName: '专业', // 页面名字
  pageNameEn: 'major', // 页面英文名
});

// 变量
const state = reactive({
  majorData: [], // 专业表数据
  deptData: [], // 院系表数据
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
  assistant: '',
  phone: '',
  department_id: '',
});

// 定义校验规则
const formRules = reactive({
  id: [
    { required: 'true', trigger: 'change', message: '请输入专业编号' },
    { pattern: /^10/, message: '专业编号要以10开头' },
    { min: 6, max: 6, message: '专业编号的长度应为6' },
    { pattern: /^10[0-9]{4}$/, message: '专业编号必须为正整数)' },
    { validator: checkId },
  ],
  name: [
    {
      required: 'true',
      message: '请输入专业名称',
      trigger: ['change', 'blur'],
    },
  ],
  assistant: [
    {
      required: 'true',
      message: '请输入辅导员姓名',
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

// 状态管理
const store = useStore();

/**
 * 获取表格数据
 */
function getData(currentPage = 1) {
  major_apis
    .read_datas({ pageIndex: currentPage, pageSize: query.pageSize })
    .then((res) => {
      state.majorData = res.data.dataList;
      state.pageTotal = res.data.count;
      // 存储关系数据
      store.commit('handleData', [page.pageNameEn, storeData(res.data.dataList)]);
    })
    .catch(() => {
      ElMessage.error(`加载${page.pageName}表数据失败!`);
    });

  // 获取下拉数据
  if (store.state.departmentData == '') {
    department_apis
      .read_datas({ pageIndex: 1, pageSize: 100 }) // 取前100数据
      .then((res) => {
        let dataList = storeData(res.data.dataList);
        state.deptData = dataList;
        store.commit('handleData', ['department', dataList]);
      })
      .catch(() => {
        ElMessage.error(`存储院系表数据失败!`);
      });
  } else {
    state.deptData = store.state.departmentData;
  }
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
      state.majorData
        .map((item) => {
          return item.id;
        })
        .indexOf(value) != -1
    ) {
      callback(new Error('专业编号已经存在'));
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