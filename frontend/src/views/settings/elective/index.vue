<script setup lang="ts">
import { reactive, onBeforeMount } from "vue";
import type { FormRules } from "element-plus";
import BaseTable from "@/components/BaseTable/index.vue";
import { readDatas } from "@/api";
import { byIdGetName } from "@/utils/handleArray";
import { PathEnum, type Query, type ElectiveForm } from "@/types/table";
import type { State } from ".";

// 变量
const state: State = reactive({
  electiveData: [], // 选课表数据
  pageTotal: 0, // 数据的总个数
  studentData: [], // 学生表数据
  courseData: [], // 课程表数据
  isDisabled: false, // 是否禁用编辑框id(可选)
  isShowSearched: false, // 是否显示被搜索的(可选)
});

// 搜索和页码
const query: Query = reactive({
  id: "",
  currentPage: 1,
  pageSize: 10,
});

// 表单对象
const formData: ElectiveForm = reactive({
  id: "",
  grade: "0",
  studentId: "",
  courseId: "",
});

// 定义校验规则
const formRules = reactive<FormRules>({
  grade: [{ pattern: /(^\s{0}$)|(^100)|(^([0]{0})([1-9]?)([0-9]))$/, message: "请输入正确的成绩分数" }],
  studentId: [{ required: true, message: "请选择学生", trigger: "change" }],
  courseId: [{ required: true, message: "请选课课程", trigger: ["change", "blur"] }],
});

/**
 * 获取表格数据
 */
const getData = async (currentPage: number = query.currentPage) => {
  let elective = readDatas({ path: PathEnum.elective, pageIndex: currentPage, pageSize: query.pageSize }); // 获取选课表数据
  let student = readDatas({ path: PathEnum.student, pageIndex: -1, pageSize: -1 }); // 获取学生表数据
  let course = readDatas({ path: PathEnum.course, pageIndex: -1, pageSize: -1 }); // 获取选课表数据

  const [{ data: electiveData }, { data: studentData }, { data: courseData }] = await Promise.all([elective, student, course]);

  state.electiveData = electiveData.list;
  state.pageTotal = electiveData.count;
  state.studentData = studentData.list;
  state.courseData = courseData.list;
};

onBeforeMount(() => {
  getData();
});

/**
 * 是否禁用编辑框id(子组件传值)
 */
const emitIsDisabled = (res: boolean) => (state.isDisabled = res);
</script>

<template>
  <base-table
    :query="query"
    :data="state.electiveData"
    :page-total="state.pageTotal"
    :form-data="formData"
    :form-rules="formRules"
    :get-data="getData"
    @emit-is-disabled="emitIsDisabled"
  >
    <!-- 暂无 -->
    <template #filter />

    <!-- 渲染表格数据 -->
    <template #tableColumn>
      <el-table-column prop="id" label="编号" width="140" align="center" />
      <el-table-column prop="grade" label="成绩" width="140" align="center" />
      <el-table-column prop="studentId" width="180" label="学生姓名" align="center">
        <template #default="scope">{{ byIdGetName(scope.row.studentId, state.studentData) }}</template>
      </el-table-column>

      <el-table-column prop="courseId" width="280" label="课程名" align="center">
        <template #default="scope">{{ byIdGetName(scope.row.courseId, state.courseData) }}</template>
      </el-table-column>
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="成绩" prop="grade">
        <el-input v-model="formData.grade" placeholder="请输入成绩(默认为0)" maxlength="3" show-word-limit />
      </el-form-item>

      <el-form-item label="学生" prop="studentId">
        <el-select v-model="formData.studentId" placeholder="学生名">
          <el-option v-for="(student, index) in state.studentData" :key="index" :label="student.name" :value="student.id" />
        </el-select>
      </el-form-item>

      <el-form-item label="课程" prop="courseId">
        <el-select v-model="formData.courseId" placeholder="课程名">
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
