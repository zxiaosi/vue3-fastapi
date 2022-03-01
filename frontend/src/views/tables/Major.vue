<script setup lang="ts">
import { reactive, onMounted } from "vue";
import { useDataStore } from "@/stores/data";
import BaseTable from "@/components/tables/BaseTable.vue";
import { read_datas, read_datas_relation } from "@/api";
import { valueList, byIdGetName } from "@/utils/handleArray";
import type { formDataType, pageType, queryType } from "@/types/table";

interface stateType {
  majorData: formDataType[];
  deptData: formDataType[];
  pageTotal: number;
  isDisabled: boolean;
  isShowSearched: boolean;
}

// 状态管理
const dataStore = useDataStore();

// 页面信息
const page: pageType = reactive({
  icon: "cascades",
  zhName: "专业表",
  enName: "major",
});

// 变量
const state: stateType = reactive({
  majorData: [], // 专业表数据
  deptData: [], // 院系表数据
  pageTotal: 0, // 数据的总个数
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
  name: "",
  assistant: "",
  phone: "",
  department_id: "",
});

// 定义校验规则
const formRules = reactive({
  id: [
    { required: "true", trigger: "change", message: "请输入专业编号" },
    { pattern: /^10/, message: "专业编号要以10开头" },
    { min: 6, max: 6, message: "专业编号的长度应为6" },
    { pattern: /^10[0-9]{4}$/, message: "专业编号必须为正整数)" },
    {
      validator: (rule: any, value: string, callback: any) => {
        let idList = valueList(dataStore.majorData, "id");
        if (!state.isDisabled && idList.indexOf(value) != -1) {
          callback(new Error("专业编号已经存在"));
        } else {
          callback(); // 验证通过
        }
      },
    },
  ],
  name: [
    {
      required: "true",
      message: "请输入专业名称",
      trigger: ["change", "blur"],
    },
    {
      validator: (rule: any, value: string, callback: any) => {
        let nameList = valueList(dataStore.majorData, "name");
        if (!state.isDisabled && nameList.indexOf(value) != -1) {
          callback(new Error("专业名字已经存在"));
        } else {
          callback(); // 验证通过
        }
      },
    },
  ],
  assistant: [
    {
      required: "true",
      message: "请输入辅导员姓名",
      trigger: ["change", "blur"],
    },
  ],
  phone: [
    {
      pattern: /^((0\d{2,3}-\d{7,8})|(1[34578]\d{9}))$/,
      message: "请输入正确的手机号",
      trigger: ["change", "blur"],
    },
  ],
  department_id: [{ required: "true", message: "请选择院系", trigger: ["change"] }],
});

/**
 * 获取表格数据
 */
const getData = async (currentPage: number = query.currentPage) => {
  // 获取专业数据
  let params = { path: page.enName, pageIndex: currentPage, pageSize: query.pageSize };
  const { data: majorData } = await read_datas(params);
  state.majorData = majorData.dataList;
  state.pageTotal = majorData.count;

  // 获取院系数据
  const { data: deptData } = await read_datas_relation("department");
  state.deptData = deptData;
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

/**
 * 获取下拉框的值
 */
const getChange = (res: string | number | undefined) => {
  // console.log("下拉框的值为--", res);
};
</script>

<template>
  <base-table
    :page="page"
    :query="query"
    :data="state.majorData"
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
        label="专业编号"
        width="120"
        align="center"
        :sortable="!state.isShowSearched"
        :sort-orders="['ascending', 'descending']"
      />
      <el-table-column prop="name" label="专业名字" width="200" align="center" />
      <el-table-column prop="assistant" label="辅导员姓名" width="120" align="center" />
      <el-table-column prop="phone" label="辅导员手机号" width="180" align="center" />
      <el-table-column prop="department_id" label="院系名字" width="200" align="center">
        <template #default="scope">{{ byIdGetName(scope.row.department_id, state.deptData) }}</template>
      </el-table-column>
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="专业编号" prop="id">
        <el-input
          v-model="formData.id"
          placeholder="请输入编号"
          maxlength="6"
          show-word-limit
          :disabled="state.isDisabled"
        />
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
      <el-form-item label="院系名字" prop="department_id">
        <el-select
          v-model="formData.department_id"
          placeholder="请选择院系"
          @change="getChange(formData.department_id)"
        >
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
