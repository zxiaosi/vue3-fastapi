<script setup lang="ts">
import { reactive, onMounted } from "vue";
import BaseTable from "@/components/tables/BaseTable.vue";
import { read_datas, read_datas_relation } from "@/api";
import { byIdGetName } from "@/utils/handleArray";
import type { formDataType, pageType, queryType } from "@/types/table";

interface stateType {
  selectCourseData: formDataType[];
  studentData: formDataType[];
  teacherData: formDataType[];
  courseData: formDataType[];
  pageTotal: number;
  isDisabled: boolean;
  isShowSearched: boolean;
}

// 页面信息
const page: pageType = reactive({
  icon: "cascades",
  zhName: "选课表",
  enName: "selectCourse",
});

// 变量
const state: stateType = reactive({
  selectCourseData: [], // 选课表数据
  pageTotal: 0, // 数据的总个数
  studentData: [], // 学生表数据
  teacherData: [], // 教师表数据
  courseData: [], // 课程表数据
  isDisabled: false, // 是否禁用编辑框id(可选)
  isShowSearched: false, // 是否显示被搜索的(可选)
});

// 搜索和页码
const query: queryType = reactive({
  id: "",
  currentPage: 1,
  pageSize: 10,
});

// 表单对象
const formData: formDataType = reactive({
  id: "",
  grade: "0",
  student_id: "",
  teacher_id: "",
  course_id: "",
});

// 定义校验规则
const formRules = reactive({
  grade: [
    { required: "true", message: "请输入成绩", trigger: ["change", "blur"] },
    { pattern: /^100|(^([0]{0})([1-9]{0,1})([0-9]{1}))$/, message: "请输入正确的成绩分数" },
  ],
  student_id: [{ required: "true", message: "请选择学生", trigger: "change" }],
  teacher_id: [{ required: "true", message: "请选择教师", trigger: "change" }],
  course_id: [{ required: "true", message: "请选课课程", trigger: ["change", "blur"] }],
});

/**
 * 获取表格数据
 */
const getData = async (currentPage: number = query.currentPage) => {
  let params = { path: page.enName, pageIndex: currentPage, pageSize: query.pageSize };
  const { data: scData } = await read_datas(params);
  state.selectCourseData = scData.dataList;
  state.pageTotal = scData.count;

  // 获取学生信息
  const { data: studentData } = await read_datas_relation("student");
  state.studentData = studentData;

  // 获取教师信息
  const { data: teacherData } = await read_datas_relation("teacher");
  state.teacherData = teacherData;

  // 获取课程信息
  const { data: courseData } = await read_datas_relation("course");
  state.courseData = courseData;
};

// 页面加载后调用函数
onMounted(() => getData());

/**
 * 是否禁用编辑框id(子组件传值)
 */
const emitIsDisabled = (res: boolean) => (state.isDisabled = res);

/**
 * 是否显示被搜索的(子组件传值)
 */
const emitIsShowSearched = (res: boolean) => (state.isShowSearched = res);
</script>

<template>
  <base-table
    :page="page"
    :query="query"
    :data="state.selectCourseData"
    :page-total="state.pageTotal"
    :form-data="formData"
    :form-rules="formRules"
    :get-data="getData"
    @emit-is-disabled="emitIsDisabled"
    @emit-is-show-searched="emitIsShowSearched"
  >
    <!-- 暂无 -->
    <template #filter />

    <!-- 渲染表格数据 -->
    <template #tableColumn>
      <el-table-column
        prop="id"
        label="编号"
        width="140"
        align="center"
        :sortable="!state.isShowSearched"
        :sort-orders="['ascending', 'descending']"
      />
      <el-table-column prop="grade" label="成绩" width="140" align="center" />
      <el-table-column prop="student_id" width="140" label="学生姓名" align="center">
        <template #default="scope">{{ byIdGetName(scope.row.student_id, state.studentData) }}</template>
      </el-table-column>

      <el-table-column prop="teacher_id" width="140" label="教师姓名" align="center">
        <template #default="scope">{{ byIdGetName(scope.row.teacher_id, state.teacherData) }}</template>
      </el-table-column>

      <el-table-column prop="course_id" width="220" label="课程名" align="center">
        <template #default="scope">{{ byIdGetName(scope.row.course_id, state.courseData) }}</template>
      </el-table-column>
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="编号" prop="id">
        <el-input
          v-model="formData.id"
          placeholder="请输入编号(自增)"
          maxlength="10"
          show-word-limit
          :disabled="state.isDisabled"
        />
      </el-form-item>
      <el-form-item label="成绩" prop="grade">
        <el-input v-model="formData.grade" placeholder="请输入成绩" maxlength="3" show-word-limit />
      </el-form-item>

      <el-form-item label="学生" prop="student_id">
        <el-select v-model="formData.student_id" placeholder="学生名">
          <el-option
            v-for="(student, index) in state.studentData"
            :key="index"
            :label="student.name"
            :value="student.id"
          />
        </el-select>
      </el-form-item>

      <el-form-item label="教师" prop="teacher_id">
        <el-select v-model="formData.teacher_id" placeholder="教师名">
          <el-option
            v-for="(teacher, index) in state.teacherData"
            :key="index"
            :label="teacher.name"
            :value="teacher.id"
          />
        </el-select>
      </el-form-item>

      <el-form-item label="课程" prop="course_id">
        <el-select v-model="formData.course_id" placeholder="课程名">
          <el-option v-for="(course, index) in state.courseData" :key="index" :label="course.name" :value="course.id" />
        </el-select>
      </el-form-item>
    </template>
  </base-table>
</template>

<style scoped>
/* 选择框长度 */
.el-form-item .el-select {
  width: 100%;
}
</style>
