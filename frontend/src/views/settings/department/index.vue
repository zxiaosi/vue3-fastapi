<script setup lang="ts">
import { reactive, onBeforeMount } from "vue";
import { useDataStore } from "@/stores/data";
import type { FormRules } from "element-plus";
import BaseTable from "@/components/BaseTable/index.vue";
import { readDatas } from "@/api";
import { PathEnum, type Query, type DeptForm } from "@/types/table";
import type { State } from ".";
import { valueList } from "@/utils/handleArray";

// 状态管理
const dataStore = useDataStore();

// 变量
const state: State = reactive({
  deptData: [], // 院系表数据
  pageTotal: 0, // 数据的总个数
  isDisabled: false, // 是否禁用编辑框id(可选)
});

// 搜索和页码
const query: Query = reactive({
  id: "",
  currentPage: 1, // 当前页
  pageSize: 10, // 每页个数
});

// 表单对象
const formData: DeptForm = reactive({
  id: "",
  name: "",
  chairman: "",
  phone: "",
});

/**
 * 对id进行验证
 */
const idValidate = (rule: any, value: string, callback: any) => {
  let idList = valueList(dataStore.departmentData, "id");
  if (!state.isDisabled && idList.indexOf(value) != -1) {
    callback(new Error("院系编号已经存在"));
  } else {
    callback(); // 验证通过
  }
};

/**
 * 对name进行验证
 */
const nameValidate = (rule: any, value: string, callback: any) => {
  let nameList = valueList(dataStore.departmentData, "name");
  if (!state.isDisabled && nameList.indexOf(value) != -1) {
    callback(new Error("院系名字已经存在"));
  } else {
    callback(); // 验证通过
  }
};

// 定义校验规则
const formRules = reactive<FormRules>({
  id: [
    { required: true, trigger: "change", message: "请输入院系编号" },
    { pattern: /^10/, message: "院系编号要以10开头" },
    { pattern: /^10[0-9]{2}$/, message: "院系编号必须是正整数且长度应为4" },
    { validator: idValidate },
  ],
  name: [{ required: true, message: "请输入院系名称", trigger: ["change", "blur"] }, { validator: nameValidate }],
  chairman: [{ required: true, message: "请输入院系主任名", trigger: ["change", "blur"] }],
  phone: [{ pattern: /^((0\d{2,3}-\d{7,8})|(1[34578]\d{9}))$/, message: "请输入正确的手机号", trigger: ["change", "blur"] }],
});

onBeforeMount(async () => {
  await getData();
});

/**
 * 获取院系表数据
 */
const getData = async (currentPage: number = query.currentPage) => {
  let params = { path: PathEnum.dept, pageIndex: currentPage, pageSize: query.pageSize };
  const { data } = await readDatas(params);
  state.deptData = data.list;
  state.pageTotal = data.count;
};

/**
 * 是否禁用编辑框id(子组件传值)
 */
const emitIsDisabled = (res: boolean) => {
  state.isDisabled = res;
};
</script>

<template>
  <base-table
    :query="query"
    :data="state.deptData"
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
      <el-table-column prop="id" label="院系编号" width="140" align="center" />
      <el-table-column prop="name" label="院系名字" width="220" align="center" />
      <el-table-column prop="chairman" label="主任名" width="140" align="center" />
      <el-table-column prop="phone" label="主任手机号" width="180" align="center" />
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="院系编号" prop="id">
        <el-input v-model="formData.id" placeholder="请输入编号" maxlength="4" show-word-limit :disabled="state.isDisabled" />
      </el-form-item>
      <el-form-item label="院系名字" prop="name">
        <el-input v-model="formData.name" placeholder="请输入名字" maxlength="20" show-word-limit />
      </el-form-item>
      <el-form-item label="主任名" prop="chairman">
        <el-input v-model="formData.chairman" placeholder="请输入主任名" maxlength="10" show-word-limit />
      </el-form-item>
      <el-form-item label="主任手机号" prop="phone">
        <el-input v-model="formData.phone" type="tel" placeholder="手机号" maxlength="11" />
      </el-form-item>
    </template>
  </base-table>
</template>
