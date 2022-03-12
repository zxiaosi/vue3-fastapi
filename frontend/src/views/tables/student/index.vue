<script setup lang="ts">
import { reactive, onMounted } from "vue";
import { useDataStore } from "@/stores/data";
import BaseTable from "@/components/baseTable/index.vue";
import { read_datas, read_datas_relation } from "@/api";
import { valueList, byIdGetName } from "@/utils/handleArray";
import { pathEnum, type queryType, type stuFormType } from "@/types/table";
import type { enumType, stateType } from ".";

// 状态管理
const dataStore = useDataStore();

// 变量
const state: stateType = reactive({
  studentData: [], // 学生表数据
  majorData: [], // 专业表数据
  pageTotal: 0, // 数据的总个数
  isDisabled: false, // 是否禁用编辑框id(可选)
  isShowSearched: false, // 是否显示被搜索的(可选)
  addOrUpdate: false, // 添加数据或更新数据
});

// 搜索和页码
const query: queryType = reactive({
  id: "",
  currentPage: 1,
  pageSize: 10,
});

// 性别枚举
const sexEnum: enumType = {
  "0": { tag: "success", name: "男" },
  "1": { tag: "danger", name: "女" },
};

// 表单对象
const formData: stuFormType = reactive({
  id: "",
  name: "",
  sex: "0",
  birthday: "",
  address: "",
  image: "",
  password: "123456",
  major_id: "",
});

// 定义校验规则
const formRules = reactive({
  id: [
    { required: "true", trigger: "change", message: "请输入学号" },
    { pattern: /^[1-9]/, message: "学号不能以0开头" },
    { min: 10, max: 10, message: "学号的长度应为10" },
    { pattern: /^[1-9][0-9]{9}$/, message: "学号必须是正整数" },
    {
      validator: (rule: any, value: string, callback: any) => {
        let idList = valueList(dataStore.studentData, "id");
        if (!state.isDisabled && idList.indexOf(value) != -1) {
          callback(new Error("院系编号已经存在"));
        } else {
          callback(); // 验证通过
        }
      },
    },
  ],
  name: [
    { required: "true", message: "请输入学生名称", trigger: ["change", "blur"] },
    {
      validator: (rule: any, value: string, callback: any) => {
        let nameList = valueList(dataStore.studentData, "name");
        if (!state.isDisabled && nameList.indexOf(value) != -1) {
          callback(new Error("院系名字已经存在"));
        } else {
          callback(); // 验证通过
        }
      },
    },
  ],
  sex: [{ required: "true", message: "请输入学生性别", trigger: "change" }],
  birthday: [{ required: "true", message: "请选择生日", trigger: "change" }],
  password: [{ message: "请输入新密码", trigger: "change" }],
  major_id: [{ required: "true", message: "请选择专业", trigger: "change" }],
});

/**
 * 获取表格数据
 */
const getData = async (currentPage: number = query.currentPage) => {
  let params = { path: pathEnum.student, pageIndex: currentPage, pageSize: query.pageSize };
  const { data: studentData } = await read_datas(params);
  state.studentData = studentData.dataList;
  state.pageTotal = studentData.count;

  const { data: majorData } = await read_datas_relation("major");
  state.majorData = majorData;
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

/**
 * 添加数据或更新数据
 */
const emitAddOrUpdate = (res: boolean) => (state.addOrUpdate = res);

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
    :data="state.studentData"
    :page-total="state.pageTotal"
    :form-data="formData"
    :form-rules="formRules"
    :get-data="getData"
    @emit-is-disabled="emitIsDisabled"
    @emit-is-show-searched="emitIsShowSearched"
    @emit-add-or-update="emitAddOrUpdate"
  >
    <!-- 暂无 -->
    <template #filter />

    <!-- 渲染表格数据 -->
    <template #tableColumn>
      <el-table-column
        prop="id"
        label="学号"
        width="140"
        align="center"
        :sortable="!state.isShowSearched"
        :sort-orders="['ascending', 'descending']"
      />
      <el-table-column prop="name" label="名字" width="120" align="center" />
      <el-table-column prop="sex" label="性别" width="80" align="center">
        <template #default="scope">
          <el-tag :type="sexEnum[scope.row.sex].tag">
            {{ sexEnum[scope.row.sex].name }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column
        prop="birthday"
        label="生日"
        width="120"
        align="center"
        :sortable="!state.isShowSearched"
        :sort-orders="['ascending', 'descending']"
      />

      <el-table-column label="头像" width="100" align="center">
        <template #default="scope">
          <el-image class="table-td-thumb" :src="scope.row.image" />
        </template>
      </el-table-column>

      <el-table-column prop="address" label="上次登录地点" width="160" align="center" />

      <el-table-column prop="major_id" label="专业名字" min-width="220" align="center">
        <template #default="scope">{{ byIdGetName(scope.row.major_id, state.majorData) }}</template>
      </el-table-column>
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="学号" prop="id">
        <el-input
          v-model="formData.id"
          placeholder="请输入学号"
          maxlength="10"
          show-word-limit
          :disabled="state.isDisabled"
        />
      </el-form-item>
      <el-form-item label="学生名字" prop="name">
        <el-input v-model="formData.name" placeholder="请输入名字" maxlength="10" show-word-limit />
      </el-form-item>

      <el-form-item label="学生性别" prop="sex">
        <el-select v-model="formData.sex" placeholder="请选择性别">
          <el-option key="1" label="男" value="0" />
          <el-option key="2" label="女" value="1" />
        </el-select>
      </el-form-item>

      <el-form-item label="学生生日" prop="birthday">
        <el-date-picker
          type="date"
          placeholder="请选择日期"
          v-model="formData.birthday"
          format="YYYY-MM-DD"
          value-format="YYYY-MM-DD"
          style="width: 100%"
        >
        </el-date-picker>
      </el-form-item>

      <el-form-item label="学生密码" prop="password">
        <el-input
          v-model="formData.password"
          :placeholder="state.addOrUpdate == true ? `默认密码为123456` : `设置新密码`"
          maxlength="20"
          show-password
        />
      </el-form-item>

      <el-form-item label="专业名字" prop="major_id">
        <el-select v-model="formData.major_id" placeholder="请选择专业" @change="getChange(formData.major_id)">
          <el-option v-for="(major, index) in state.majorData" :key="index" :label="major.name" :value="major.id" />
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

.table-td-thumb {
  display: block;
  margin: auto;
  width: 35px;
  height: 35px;
}
</style>
