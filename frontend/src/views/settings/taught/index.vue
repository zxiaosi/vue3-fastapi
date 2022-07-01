<script setup lang="ts">
import { reactive, onBeforeMount } from "vue";
import type { FormRules } from "element-plus";
import BaseTable from "@/components/BaseTable/index.vue";
import { readDatas } from "@/api";
import { byIdGetName } from "@/utils/handleArray";
import { PathEnum, type Query, type TaughtForm } from "@/types/table";
import type { State } from ".";

// 变量
const state: State = reactive({
  taughtData: [], // 授课表数据
  pageTotal: 0, // 数据的总个数
  teacherData: [], // 教师表数据
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
const formData: TaughtForm = reactive({
  id: "",
  teacherId: "",
  courseId: "",
});

// 定义校验规则
const formRules = reactive<FormRules>({
  teacherId: [{ required: true, message: "请选择教师", trigger: "change" }],
  courseId: [{ required: true, message: "请选课课程", trigger: ["change", "blur"] }],
});

/**
 * 获取表格数据
 */
const getData = async (currentPage: number = query.currentPage) => {
  let taught = readDatas({ path: PathEnum.taught, pageIndex: currentPage, pageSize: query.pageSize }); // 获取授课表数据
  let teacher = readDatas({ path: PathEnum.teacher, pageIndex: -1, pageSize: -1 }); // 获取教师表数据
  let course = readDatas({ path: PathEnum.course, pageIndex: -1, pageSize: -1 }); // 获取选课表数据

  const [{ data: taughtData }, { data: teacherData }, { data: courseData }] = await Promise.all([taught, teacher, course]);

  state.taughtData = taughtData.list;
  state.pageTotal = taughtData.count;
  state.teacherData = teacherData.list;
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
    :data="state.taughtData"
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

      <el-table-column prop="teacherId" width="200" label="教师姓名" align="center">
        <template #default="scope">{{ byIdGetName(scope.row.teacherId, state.teacherData) }}</template>
      </el-table-column>

      <el-table-column prop="courseId" width="300" label="课程名" align="center">
        <template #default="scope">{{ byIdGetName(scope.row.courseId, state.courseData) }}</template>
      </el-table-column>
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="教师" prop="teacherId">
        <el-select v-model="formData.teacherId" placeholder="教师名">
          <el-option v-for="(teacher, index) in state.teacherData" :key="index" :label="teacher.name" :value="teacher.id" />
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
