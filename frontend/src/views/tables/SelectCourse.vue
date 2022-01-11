<template>
  <base-table :page="page" :query="query" :data="state.selectCourseData"
    :page-total="state.pageTotal" :form-data="formData" :form-rules="formRules" :get-data="getData"
    :apis="selectCourse_apis" @emit-is-disabled="emitIsDisabled"
    @emit-is-show-searched="emitIsShowSearched">

    <!-- 暂无 -->
    <template #filter />

    <!-- 渲染表格数据 -->
    <template #tableColumn>
      <el-table-column prop="id" label="编号" width="140" align="center"
        :sortable="!state.isShowSearched" :sort-orders="['ascending', 'descending']" />
      <el-table-column prop="grade" label="成绩" width="140" align="center" />
      <el-table-column prop="student_id" width="140" label="学生姓名" align="center">
        <template
          #default="scope">{{byIdGetName(scope.row.student_id, state.studentData)}}</template>
      </el-table-column>

      <el-table-column prop="teacher_id" width="140" label="教师姓名" align="center">
        <template
          #default="scope">{{byIdGetName(scope.row.teacher_id, state.teacherData)}}</template>
      </el-table-column>

      <el-table-column prop="course_id" min-width="220" label="课程名" align="center">
        <template #default="scope">{{byIdGetName(scope.row.course_id, state.courseData)}}</template>
      </el-table-column>
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="编号" prop="id" v-show="!state.addOrUpdate">
        <el-input v-model="formData.id" placeholder="请输入编号(自增)" maxlength="10" show-word-limit
          :disabled=state.isDisabled />
      </el-form-item>
      <el-form-item label="成绩" prop="grade">
        <el-input v-model="formData.grade" placeholder="请输入成绩" maxlength="3" show-word-limit />
      </el-form-item>

      <el-form-item label="学生" prop="student_id">
        <el-select v-model="formData.student_id" placeholder="学生名">
          <el-option v-for="(student, index) in state.studentData" :key=index :label=student.name
            :value=student.id />
        </el-select>
      </el-form-item>

      <el-form-item label="教师" prop="teacher_id">
        <el-select v-model="formData.teacher_id" placeholder="教师名">
          <el-option v-for="(teacher, index) in state.teacherData" :key=index :label=teacher.name
            :value=teacher.id />
        </el-select>
      </el-form-item>

      <el-form-item label="课程" prop="course_id">
        <el-select v-model="formData.course_id" placeholder="课程名">
          <el-option v-for="(course, index) in state.courseData" :key=index :label=course.name
            :value=course.id />
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
import selectCourse_apis from '@api/selectCourse';
import student_apis from '@api/student';
import teacher_apis from '@api/teacher';
import course_apis from '@api/course';
import { byIdGetName } from '@utils/byIdGetName';

// 页面配置
const page = reactive({
  iconName: 'cascades', // 页面icon名字
  pageName: '选课', // 页面名字
  pageNameEn: 'selectCourse', // 页面英文名
});

// 变量
const state = reactive({
  selectCourseData: [], // 选课表数据
  pageTotal: 0, // 数据的总个数
  studentData: [], // 学生表数据
  teacherData: [], // 教师表数据
  courseData: [], // 课程表数据
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
  grade: 0,
  student_id: '',
  teacher_id: '',
  course_id: '',
});

// 定义校验规则
const formRules = reactive({
  grade: [
    { required: 'true', message: '请输入成绩', trigger: ['change', 'blur'] },
    {
      pattern: /^100|(^([0]{0})([1-9]{0,1})([0-9]{1}))$/,
      message: '请输入正确的成绩分数',
    },
  ],
  student_id: [{ required: 'true', message: '请选择学生', trigger: 'change' }],
  teacher_id: [{ required: 'true', message: '请选择教师', trigger: 'change' }],
  course_id: [
    { required: 'true', message: '请选课课程', trigger: ['change', 'blur'] },
  ],
});

// 状态管理
const store = useStore();

/**
 * 获取表格数据
 */
function getData(currentPage = 1) {
  selectCourse_apis
    .read_datas(currentPage)
    .then((res) => {
      state.selectCourseData = res.data.dataList;
      state.pageTotal = res.data.count;
    })
    .catch(() => {
      ElMessage.error(`加载${page.pageName}表数据失败!`);
    });

  // 获取学生信息
  if (store.state.studentData == '') {
    student_apis
      .student_relation()
      .then((res) => {
        state.studentData = res.data;
        store.commit('handleData', ['student', res.data]);
      })
      .catch(() => {
        ElMessage.error(`存储学生表数据失败!`);
      });
  } else {
    state.studentData = store.state.studentData;
  }

  // 获取教师信息
  if (store.state.teacherData == '') {
    teacher_apis
      .teacher_relation()
      .then((res) => {
        state.teacherData = res.data;
        store.commit('handleData', ['teacher', res.data]);
      })
      .catch(() => {
        ElMessage.error(`存储教师表数据失败!`);
      });
  } else {
    state.teacherData = store.state.teacherData;
  }

  // 获取课程信息
  if (store.state.courseData == '') {
    course_apis
      .course_relation()
      .then((res) => {
        state.courseData = res.data;
        store.commit('handleData', ['course', res.data]);
      })
      .catch(() => {
        ElMessage.error(`存储课程表数据失败!`);
      });
  } else {
    state.courseData = store.state.courseData;
  }
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
</script>

<style scoped>
/* 选择框长度 */
.el-form-item .el-select {
  width: 100%;
}
</style>