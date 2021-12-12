<template>
  <base-table :page="page" :query="query" :data="state.selectCourseData" :form="form"
    :get-data="getData" :apis="selectCourse_apis" @emit-is-disabled="emitIsDisabled"
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
        <el-input v-model="form.data.id" placeholder="请输入编号(自增)" maxlength="10" show-word-limit
          :disabled=state.isDisabled />
      </el-form-item>
      <el-form-item label="成绩" prop="grade">
        <el-input v-model="form.data.grade" placeholder="请输入成绩(默认为0)" maxlength="3"
          show-word-limit />
      </el-form-item>

      <el-form-item label="学生" prop="student_id">
        <el-select v-model="form.data.student_id" placeholder="学生名">
          <el-option v-for="(student, index) in state.studentData" :key=index :label=student.name
            :value=student.id />
        </el-select>
      </el-form-item>

      <el-form-item label="教师" prop="teacher_id">
        <el-select v-model="form.data.teacher_id" placeholder="教师名">
          <el-option v-for="(teacher, index) in state.teacherData" :key=index :label=teacher.name
            :value=teacher.id />
        </el-select>
      </el-form-item>

      <el-form-item label="课程" prop="course_id">
        <el-select v-model="form.data.course_id" placeholder="课程名">
          <el-option v-for="(course, index) in state.courseData" :key=index :label=course.name
            :value=course.id />
        </el-select>
      </el-form-item>
    </template>

  </base-table>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'selectcourse',
});
</script>

<script setup>
import { reactive, onMounted } from 'vue';
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
});

// 变量
const state = reactive({
  selectCourseData: [], // 选课表数据
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

// 表单信息
const form = reactive({
  // 表单对象
  data: {
    id: '',
    grade: '',
    student_id: '',
    teacher_id: '',
    course_id: '',
  },
  // 定义校验规则
  rules: {
    grade: [
      { message: '请输入成绩', trigger: ['change', 'blur'] },
      {
        pattern: /^100|(^([1-9]{0,1})([0-9]{1}))$/,
        message: '请输入正确的成绩分数',
      },
    ],
    student_id: [
      { required: 'true', message: '请选择学生', trigger: 'change' },
    ],
    teacher_id: [
      { required: 'true', message: '请选择教师', trigger: 'change' },
    ],
    course_id: [
      { required: 'true', message: '请选课课程', trigger: ['change', 'blur'] },
    ],
  },
});

/**
 * 获取表格数据
 */
function getData() {
  selectCourse_apis
    .read_datas()
    .then((res) => {
      state.selectCourseData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载选课信息数据失败！');
    });

  // 获取学生信息
  student_apis
    .read_datas()
    .then((res) => {
      state.studentData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载学生信息数据失败！');
    });

  // 获取教师信息
  teacher_apis
    .read_datas()
    .then((res) => {
      state.teacherData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载教师信息数据失败！');
    });

  // 获取课程信息
  course_apis
    .read_datas()
    .then((res) => {
      state.courseData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载课程信息数据失败！');
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
</script>

<style scoped>
/* 选择框长度 */
.el-form-item .el-select {
  width: 100%;
}
</style>