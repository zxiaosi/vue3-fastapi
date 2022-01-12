<template>
  <base-table :page="page" :query="query" :data="state.studentData" :page-total="state.pageTotal"
    :form-data="formData" :form-rules="formRules" :get-data="getData" :apis="student_apis"
    @emit-is-disabled="emitIsDisabled" @emit-is-show-searched="emitIsShowSearched">

    <!-- 暂无 -->
    <template #filter />

    <!-- 渲染表格数据 -->
    <template #tableColumn>
      <el-table-column prop="id" label="学号" width="140" align="center"
        :sortable="!state.isShowSearched" :sort-orders="['ascending', 'descending']" />
      <el-table-column prop="name" label="学生名字" width="140" align="center" />
      <el-table-column prop="sex" label="学生性别" width="140" align="center">
        <template #default="scope">
          <el-tag :type="scope.row.sex === 'man' ? 'success': 'danger'">
            {{ scope.row.sex=== 'man' ? '男': '女' }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="birthday" label="学生生日" width="220" align="center"
        :sortable="!state.isShowSearched" :sort-orders="['ascending', 'descending']" />

      <el-table-column prop="major_id" label="专业名字" min-width="220" align="center">
        <template #default="scope">{{byIdGetName(scope.row.major_id, state.majorData)}}</template>
      </el-table-column>
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="学号" prop="id">
        <el-input v-model="formData.id" placeholder="请输入学号" maxlength="10" show-word-limit
          :disabled=state.isDisabled />
      </el-form-item>
      <el-form-item label="学生名字" prop="name">
        <el-input v-model="formData.name" placeholder="请输入名字" maxlength="10" show-word-limit />
      </el-form-item>

      <el-form-item label="学生性别" prop="sex">
        <el-select v-model="formData.sex" placeholder="请选择性别">
          <el-option key="1" label="男" value="man" />
          <el-option key="2" label="女" value="woman" />
        </el-select>
      </el-form-item>

      <el-form-item label="学生生日">
        <el-form-item prop="birthday">
          <el-date-picker type="date" placeholder="请选择日期" v-model="formData.birthday"
            format="YYYY-MM-DD" value-format="YYYY-MM-DD" style="width: 100%;">
          </el-date-picker>
        </el-form-item>
      </el-form-item>

      <el-form-item label="学生密码" prop="password">
        <el-input v-model="formData.password" placeholder="请输入密码" maxlength="20" show-word-limit />
      </el-form-item>

      <el-form-item label="专业名字" prop="major_id">
        <el-select v-model="formData.major_id" placeholder="请选择专业"
          @change="getChange(formData.major_id)">
          <el-option v-for="(major, index) in state.majorData" :key=index :label=major.name
            :value=major.id />
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
import student_apis from '@api/student';
import major_apis from '@api/major';
import { byIdGetName } from '@utils/byIdGetName';

// 页面配置
const page = reactive({
  iconName: 'cascades', // 页面icon名字
  pageName: '学生', // 页面名字
  pageNameEn: 'student', // 页面英文名
});

// 变量
const state = reactive({
  studentData: [], // 学生表数据
  majorData: [], // 专业表数据
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
  sex: '',
  birthday: '',
  password: '',
  major_id: '',
});

// 定义校验规则
const formRules = reactive({
  id: [
    { required: 'true', trigger: 'change', message: '请输入学号' },
    { pattern: /^[1-9]/, message: '学号不能以0开头' },
    { min: 10, max: 10, message: '学号的长度应为10' },
    { pattern: /^[1-9][0-9]{9}$/, message: '学号必须是正整数' },
    { validator: checkId },
  ],
  name: [
    {
      required: 'true',
      message: '请输入学生名称',
      trigger: ['change', 'blur'],
    },
  ],
  sex: [{ required: 'true', message: '请输入学生性别', trigger: 'change' }],
  birthday: [{ required: 'true', message: '请选择生日', trigger: 'change' }],
  password: [
    { required: 'true', message: '请输入密码', trigger: ['change', 'blur'] },
  ],
  major_id: [{ required: 'true', message: '请选择专业', trigger: ['change'] }],
});

// 状态管理
const store = useStore();

/**
 * 获取表格数据
 */
function getData(currentPage = 1) {
  student_apis
    .read_datas(currentPage, query.pageSize)
    .then((res) => {
      state.studentData = res.data.dataList;
      state.pageTotal = res.data.count;
    })
    .catch(() => {
      ElMessage.error(`加载${page.pageName}表数据失败!`);
    });

  // 获取专业信息
  if (store.state.majorData == '') {
    major_apis
      .major_relation()
      .then((res) => {
        state.majorData = res.data;
        store.commit('handleData', ['major', res.data]);
      })
      .catch(() => {
        ElMessage.error(`存储专业表数据失败!`);
      });
  } else {
    state.majorData = store.state.majorData;
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
      state.studentData
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
/* 选择框长度 */
.el-form-item .el-select {
  width: 100%;
}
</style>