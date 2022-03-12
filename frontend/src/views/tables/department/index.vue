<script setup lang="ts">
import { reactive, onMounted } from "vue";
import { useDataStore } from "@/stores/data";
import BaseTable from "@/components/baseTable/index.vue";
import { read_datas } from "@/api";
import type { stateType } from ".";
import { pathEnum, type queryType, type deptFormType } from "@/types/table";
import { valueList } from "@/utils/handleArray";

// 状态管理
const dataStore = useDataStore();

// 变量
const state: stateType = reactive({
  deptData: [], // 院系表数据
  pageTotal: 0, // 数据的总个数
  isDisabled: false, // 是否禁用编辑框id(可选)
  isShowSearched: false, // 是否显示被搜索的(可选)
});

// 搜索和页码
const query: queryType = reactive({
  id: "",
  currentPage: 1, // 当前页
  pageSize: 10, // 每页个数
});

// 表单对象
const formData: deptFormType = reactive({
  id: "",
  name: "",
  chairman: "",
  phone: "",
});

// 定义校验规则
const formRules = reactive({
  id: [
    { required: "true", trigger: "change", message: "请输入院系编号" },
    { pattern: /^10/, message: "院系编号要以10开头" },
    { min: 4, max: 4, message: "院系编号的长度应为4" },
    { pattern: /^10[0-9]{2}$/, message: "院系编号必须是正整数" },
    {
      validator: (rule: any, value: string, callback: any) => {
        let idList = valueList(dataStore.departmentData, "id");
        if (!state.isDisabled && idList.indexOf(value) != -1) {
          callback(new Error("院系编号已经存在"));
        } else {
          callback(); // 验证通过
        }
      },
    },
  ],
  name: [
    {
      required: "true",
      message: "请输入院系名称",
      trigger: ["change", "blur"],
    },
    {
      validator: (rule: any, value: string, callback: any) => {
        let nameList = valueList(dataStore.departmentData, "name");
        if (!state.isDisabled && nameList.indexOf(value) != -1) {
          callback(new Error("院系名字已经存在"));
        } else {
          callback(); // 验证通过
        }
      },
    },
  ],
  chairman: [
    {
      required: "true",
      message: "请输入院系主任名",
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
});

/**
 * 获取院系表数据
 */
const getData = async (currentPage: number = query.currentPage) => {
  let params = { path: pathEnum.dept, pageIndex: currentPage, pageSize: query.pageSize };
  const { data } = await read_datas(params);
  state.deptData = data.dataList;
  state.pageTotal = data.count;
};

// 页面加载后调用函数
onMounted(async () => await getData());

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
    :query="query"
    :data="state.deptData"
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
        label="院系编号"
        width="140"
        align="center"
        :sortable="!state.isShowSearched"
        :sort-orders="['ascending', 'descending']"
      />
      <el-table-column prop="name" label="院系名字" width="220" align="center" />
      <el-table-column prop="chairman" label="主任名" width="140" align="center" />
      <el-table-column prop="phone" label="主任手机号" width="180" align="center" />
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="院系编号" prop="id">
        <el-input
          v-model="formData.id"
          placeholder="请输入编号"
          maxlength="4"
          show-word-limit
          :disabled="state.isDisabled"
        />
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
