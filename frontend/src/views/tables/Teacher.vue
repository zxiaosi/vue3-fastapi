<template>
  <base-table :page="page" :query="query" :data="state.teacherData" :page-total="state.pageTotal"
    :form-data="formData" :form-rules="formRules" :get-data="getData" :apis="teacher_apis"
    @emit-is-disabled="emitIsDisabled" @emit-is-show-searched="emitIsShowSearched">

    <!-- 暂无 -->
    <template #filter />

    <!-- 渲染表格数据 -->
    <template #tableColumn>
      <el-table-column prop="id" label="职工号" width="140" align="center"
        :sortable="!state.isShowSearched" :sort-orders="['ascending', 'descending']" />
      <el-table-column prop="name" label="教师名字" width="140" align="center" />

      <el-table-column prop="sex" label="教师性别" width="140" align="center">
        <template #default="scope">
          <el-tag :type="scope.row.sex === 'man' ? 'success': 'danger'">
            {{ scope.row.sex=== 'man' ? '男': '女' }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column prop="birthday" label="教师生日" width="220" align="center"
        :sortable="!state.isShowSearched" :sort-orders="['ascending', 'descending']" />

      <el-table-column prop="education" label="教师学历" width="140" align="center">
        <template #default="scope">
          <el-tag :type="scope.row.education === 'Bachelor' 
              ? 'success' : scope.row.education === 'Master' 
              ? '' : 'warning'">
            {{
                scope.row.education === 'Bachelor' 
                ? '学士' : scope.row.education === 'Master' 
                ? '硕士' : '博士'
              }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column prop="title" label="教师职称" width="140" align="center">
        <template #default="scope">
          <el-tag :type="
                      scope.row.title === 'Assistant' 
                      ? 'success' : scope.row.title === 'Lecturer' 
                      ? 'danger' : scope.row.title === 'Associate' 
                      ? '' : 'warning'
                    ">
            {{
                scope.row.title === 'Assistant' 
                ? '助教' : scope.row.title === 'Lecturer' 
                ? '讲师' : scope.row.title === 'Associate'
                ? '副教授': '教授'
              }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column prop="department_id" label="院系名字" min-width="220" align="center">
        <template
          #default="scope">{{byIdGetName(scope.row.department_id, state.deptData)}}</template>
      </el-table-column>
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="职工号" prop="id">
        <el-input v-model="formData.id" placeholder="请输入职工号" maxlength="6" show-word-limit
          :disabled=state.isDisabled />
      </el-form-item>
      <el-form-item label="教师名字" prop="name">
        <el-input v-model="formData.name" placeholder="请输入名字" maxlength="10" show-word-limit />
      </el-form-item>

      <el-form-item label="教师性别" prop="sex">
        <el-select v-model="formData.sex" placeholder="请选择性别">
          <el-option key="1" label="男" value="man" />
          <el-option key="2" label="女" value="woman" />
        </el-select>
      </el-form-item>

      <el-form-item label="教师生日">
        <el-form-item prop="birthday">
          <el-date-picker type="date" placeholder="请选择日期" v-model="formData.birthday"
            format="YYYY-MM-DD" value-format="YYYY-MM-DD" style="width: 100%;">
          </el-date-picker>
        </el-form-item>
      </el-form-item>

      <el-form-item label="教师密码" prop="password">
        <el-input v-model="formData.password" placeholder="请输入密码" maxlength="20" show-word-limit />
      </el-form-item>

      <el-form-item label="教师学历" prop="education">
        <el-select v-model="formData.education" placeholder="请选择学历">
          <el-option key="1" label="学士" value="Bachelor" />
          <el-option key="2" label="硕士" value="Master" />
          <el-option key="3" label="博士" value="Doctor" />
        </el-select>
      </el-form-item>

      <el-form-item label="教师职称" prop="title">
        <el-select v-model="formData.title" placeholder="请选择职称">
          <el-option key="1" label="助教" value="Assistant" />
          <el-option key="2" label="讲师" value="Lecturer" />
          <el-option key="3" label="副教授" value="Associate" />
          <el-option key="4" label="教授" value="Professor" />
        </el-select>
      </el-form-item>

      <el-form-item label="院系名字" prop="department_id">
        <el-select v-model="formData.department_id" placeholder="请选择院系"
          @change="getChange(formData.department_id)">
          <el-option v-for="(dept, index) in state.deptData" :key=index :label=dept.name
            :value=dept.id />
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
import teacher_apis from '@api/teacher';
import department_apis from '@api/department';
import { byIdGetName } from '@utils/byIdGetName';

// 页面配置
const page = reactive({
  iconName: 'cascades', // 页面icon名字
  pageName: '教师', // 页面名字
  pageNameEn: 'teacher', // 页面英文名
});

// 变量
const state = reactive({
  teacherData: [], // 教师表数据
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
  sex: '',
  birthday: '',
  password: '',
  education: '',
  title: '',
  department_id: '',
});

// 定义校验规则
const formRules = reactive({
  id: [
    { required: 'true', trigger: 'change', message: '请输入职工号' },
    { pattern: /^[1-9]/, message: '职工号不能以0开头' },
    { min: 6, max: 6, message: '职工号的长度应为6' },
    { pattern: /^[1-9][0-9]{5}$/, message: '职工号必须是正整数' },
    { validator: checkId },
  ],
  name: [
    {
      required: 'true',
      message: '请输入教师名称(最大长度为10)',
      trigger: ['change', 'blur'],
    },
  ],
  sex: [{ required: 'true', message: '请输入教师性别', trigger: 'change' }],
  birthday: [{ required: 'true', message: '请选择生日', trigger: 'change' }],
  password: [
    { required: 'true', message: '请输入密码', trigger: ['change', 'blur'] },
  ],
  education: [
    { required: 'true', message: '请选择教师学历', trigger: 'change' },
  ],
  title: [{ required: 'true', message: '请选择教师职称', trigger: 'change' }],
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
  teacher_apis
    .read_datas(currentPage, query.pageSize)
    .then((res) => {
      state.teacherData = res.data.dataList;
      state.pageTotal = res.data.count;
    })
    .catch(() => {
      ElMessage.error(`加载${page.pageName}表数据失败!`);
    });

  // 获取院系信息
  if (store.state.departmentData == '') {
    department_apis
      .department_relation()
      .then((res) => {
        state.deptData = res.data;
        store.commit('handleData', ['department', res.data]);
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
      state.teacherData
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