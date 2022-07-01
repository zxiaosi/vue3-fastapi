<script setup lang="ts">
import { reactive, onBeforeMount } from "vue";
import { useDataStore } from "@/stores/data";
import type { FormRules } from "element-plus";
import BaseTable from "@/components/BaseTable/index.vue";
import { readDatas } from "@/api";
import type { State } from ".";
import { PathEnum, type Query, type MajorForm } from "@/types/table";
import { valueList, byIdGetName } from "@/utils/handleArray";

// 状态管理
const dataStore = useDataStore();

// 变量
const state: State = reactive({
  majorData: [], // 专业表数据
  deptData: [], // 院系表数据
  pageTotal: 0, // 数据的总个数
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
const formData: MajorForm = reactive({
  id: "",
  name: "",
  assistant: "",
  phone: "",
  departmentId: "",
});

/**
 * 对id进行验证
 */
const idValidate = (rule: any, value: string, callback: any) => {
  let idList = valueList(dataStore.majorData, "id");
  if (!state.isDisabled && idList.indexOf(value) != -1) {
    callback(new Error("专业编号已经存在"));
  } else {
    callback(); // 验证通过
  }
};

/**
 * 对name进行验证
 */
const nameValidate = (rule: any, value: string, callback: any) => {
  let nameList = valueList(dataStore.majorData, "name");
  if (!state.isDisabled && nameList.indexOf(value) != -1) {
    callback(new Error("专业名字已经存在"));
  } else {
    callback(); // 验证通过
  }
};

// 定义校验规则
const formRules = reactive<FormRules>({
  id: [
    { required: true, trigger: "change", message: "请输入专业编号" },
    { pattern: /^10/, message: "专业编号要以10开头" },
    { pattern: /^10[0-9]{4}$/, message: "专业编号必须为正整数且长度为6" },
    { validator: idValidate },
  ],
  name: [{ required: true, message: "请输入专业名称", trigger: ["change", "blur"] }, { validator: nameValidate }],
  assistant: [{ required: true, message: "请输入辅导员姓名", trigger: ["change", "blur"] }],
  phone: [{ pattern: /^((0\d{2,3}-\d{7,8})|(1[34578]\d{9}))$/, message: "请输入正确的手机号", trigger: ["change", "blur"] }],
  departmentId: [{ required: true, message: "请选择院系", trigger: ["change"] }],
});

/**
 * 获取表格数据
 */
const getData = async (currentPage: number = query.currentPage) => {
  let dept = readDatas({ path: PathEnum.dept, pageIndex: -1, pageSize: -1 }); // 获取院系数据
  let major = readDatas({ path: PathEnum.major, pageIndex: currentPage, pageSize: query.pageSize }); // 获取专业数据

  const [{ data: deptData }, { data: majorData }] = await Promise.all([dept, major]);

  state.majorData = majorData.list;
  state.pageTotal = majorData.count;
  state.deptData = deptData.list;
};

// 页面加载后调用函数
onBeforeMount(async () => {
  await getData();
});

/**
 * 是否禁用编辑框id(子组件传值)
 */
const emitIsDisabled = (res: boolean) => (state.isDisabled = res);
/**
 * 获取下拉框的值
 */
const getChange = (res: string | number | undefined) => {
  // console.log("下拉框的值为--", res);
};
</script>

<template>
  <base-table
    :query="query"
    :data="state.majorData"
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
      <el-table-column prop="id" label="专业编号" width="120" align="center" />
      <el-table-column prop="name" label="专业名字" width="200" align="center" />
      <el-table-column prop="assistant" label="辅导员姓名" width="120" align="center" />
      <el-table-column prop="phone" label="辅导员手机号" width="180" align="center" />
      <el-table-column prop="departmentId" label="院系名字" width="200" align="center">
        <template #default="scope">{{ byIdGetName(scope.row.departmentId, state.deptData) }}</template>
      </el-table-column>
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="专业编号" prop="id">
        <el-input v-model="formData.id" placeholder="请输入编号" maxlength="6" show-word-limit :disabled="state.isDisabled" />
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
      <el-form-item label="院系名字" prop="departmentId">
        <el-select v-model="formData.departmentId" placeholder="请选择院系" @change="getChange(formData.departmentId)">
          <el-option v-for="(dept, index) in state.deptData" :key="index" :label="dept.name" :value="dept.id" />
        </el-select>
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
