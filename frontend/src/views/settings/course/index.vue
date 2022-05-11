<script setup lang="ts">
import { reactive, onBeforeMount } from "vue";
import { useDataStore } from "@/stores/data";
import type { FormRules } from "element-plus";
import BaseTable from "@/components/BaseTable/index.vue";
import { readDatas } from "@/api";
import { valueList } from "@/utils/handleArray";
import type { State } from ".";
import { PathEnum, type Query, type CourseForm } from "@/types/table";

// 状态管理
const dataStore = useDataStore();

// 变量
const state: State = reactive({
  courseData: [], // 课程表数据
  pageTotal: 0, // 数据的总个数
  isDisabled: false, // 是否禁用编辑框id(可选)
});

// 搜索和页码
const query: Query = reactive({
  id: "",
  currentPage: 1,
  pageSize: 10,
});

// 表单对象
const formData: CourseForm = reactive({
  id: "",
  name: "",
  credit: "",
  period: "",
});

/**
 * 对id进行验证
 */
const idValidate = (rule: any, value: string, callback: any) => {
  let idList = valueList(dataStore.courseData, "id");
  if (!state.isDisabled && idList.indexOf(value) != -1) {
    callback(new Error("课程编号已经存在"));
  } else {
    callback(); // 验证通过
  }
};

/**
 * 对name进行验证
 */
const nameValidate = (rule: any, value: string, callback: any) => {
  let nameList = valueList(dataStore.courseData, "name");
  if (!state.isDisabled && nameList.indexOf(value) != -1) {
    callback(new Error("课程名字已经存在"));
  } else {
    callback(); // 验证通过
  }
};

// 定义校验规则
const formRules = reactive<FormRules>({
  id: [
    { required: true, trigger: "change", message: "请输入课程编号" },
    { pattern: /^[1-9]/, message: "课程编号不能以0开头" },
    { pattern: /^[1-9][0-9]{3}$/, message: "课程编号必须是正整数且长度应为4" },
    { validator: idValidate },
  ],
  name: [{ required: true, message: "请输入课程名称", trigger: ["change", "blur"] }, { validator: nameValidate }],
  credit: [
    { required: true, message: "请输入学分", trigger: ["change", "blur"] },
    { pattern: /^[1-4]$/, message: "学分应在1-4之间" },
  ],
  period: [
    { required: true, message: "请输入课时", trigger: ["change", "blur"] },
    { pattern: /^[1-9]$|^([1-2][0-9])$|^3[0-2]$/, message: "学时应在1-32之间" },
  ],
});

/**
 * 获取课程表数据
 */
const getData = async (currentPage: number = query.currentPage) => {
  let params = { path: PathEnum.course, pageIndex: currentPage, pageSize: query.pageSize };
  const { data } = await readDatas(params);
  state.courseData = data.list;
  state.pageTotal = data.count;
};

// 页面加载后调用函数
onBeforeMount(async () => {
  await getData();
});

/**
 * 是否禁用编辑框id(子组件传值)
 */
const emitIsDisabled = (res: boolean) => (state.isDisabled = res);
</script>

<template>
  <base-table
    :query="query"
    :data="state.courseData"
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
      <el-table-column prop="id" label="课程编号" width="140" align="center" />
      <el-table-column prop="name" label="课程名字" width="280" align="center" />
      <el-table-column prop="credit" label="学分" width="140" align="center" />
      <el-table-column prop="period" label="课时" width="140" align="center" />
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="课程编号" prop="id">
        <el-input v-model="formData.id" placeholder="请输入编号" maxlength="4" show-word-limit :disabled="state.isDisabled" />
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

<style scoped>
/* 选中框长度 */
.el-form-item .el-select {
  width: 100%;
}
</style>
