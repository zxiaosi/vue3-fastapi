<script setup lang="ts">
import { reactive, onBeforeMount } from "vue";
import { useDataStore } from "@/stores/data";
import type { FormRules } from "element-plus";
import BaseTable from "@/components/BaseTable/index.vue";
import { readDatas } from "@/api";
import { valueList, byIdGetName } from "@/utils/handleArray";
import { PathEnum, type Query, type StudentForm } from "@/types/table";
import { type State, SexEnum, TagEnum } from ".";

// 状态管理
const dataStore = useDataStore();

// 变量
const state: State = reactive({
  studentData: [], // 学生表数据
  majorData: [], // 专业表数据
  pageTotal: 0, // 数据的总个数
  isDisabled: false, // 是否禁用编辑框id(可选)
  isShowSearched: false, // 是否显示被搜索的(可选)
  addOrUpdate: false, // 添加数据或更新数据
});

// 搜索和页码
const query: Query = reactive({
  id: "",
  currentPage: 1,
  pageSize: 10,
});

// 表单对象
const formData: StudentForm = reactive({
  id: "",
  name: "",
  sex: "0",
  birthday: "",
  address: "",
  image: "",
  password: "123456",
  majorId: "",
});

/**
 * 对id进行验证
 */
const idValidate = (rule: any, value: string, callback: any) => {
  let idList = valueList(dataStore.studentData, "id");
  if (!state.isDisabled && idList.indexOf(value) != -1) {
    callback(new Error("学号已经存在"));
  } else {
    callback(); // 验证通过
  }
};

/**
 * 对name进行验证
 */
const nameValidate = (rule: any, value: string, callback: any) => {
  let nameList = valueList(dataStore.studentData, "name");
  if (!state.isDisabled && nameList.indexOf(value) != -1) {
    callback(new Error("学生名字已经存在"));
  } else {
    callback(); // 验证通过
  }
};

// 定义校验规则
const formRules = reactive<FormRules>({
  id: [
    { required: true, trigger: "change", message: "请输入学号" },
    { pattern: /^[1-9]/, message: "学号不能以0开头" },
    { pattern: /^[1-9][0-9]{9}$/, message: "学号必须是正整数且长度应为10" },
    { validator: idValidate },
  ],
  name: [{ required: true, message: "请输入学生名称", trigger: ["change", "blur"] }, { validator: nameValidate }],
  sex: [{ required: true, message: "请输入学生性别", trigger: "change" }],
  birthday: [{ required: true, message: "请选择生日", trigger: "change" }],
  password: [{ message: "请输入新密码", trigger: "change" }],
  majorId: [{ required: true, message: "请选择专业", trigger: "change" }],
});

/**
 * 获取表格数据
 */
const getData = async (currentPage: number = query.currentPage) => {
  let major = readDatas({ path: PathEnum.major, pageIndex: -1, pageSize: -1 }); // 获取专业数据
  let student = readDatas({ path: PathEnum.student, pageIndex: currentPage, pageSize: query.pageSize }); // 获取学生数据

  const [{ data: majorData }, { data: studentData }] = await Promise.all([major, student]);

  state.studentData = studentData.list;
  state.pageTotal = studentData.count;
  state.majorData = majorData.list;
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
    @emit-add-or-update="emitAddOrUpdate"
  >
    <!-- 暂无 -->
    <template #filter />

    <!-- 渲染表格数据 -->
    <template #tableColumn>
      <el-table-column prop="id" label="学号" width="140" align="center" />
      <el-table-column prop="name" label="名字" width="120" align="center" />
      <el-table-column prop="sex" label="性别" width="80" align="center">
        <template #default="scope">
          <el-tag :type="TagEnum[scope.row.sex]">
            {{ SexEnum[scope.row.sex] }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="birthday" label="生日" width="120" align="center" />

      <el-table-column prop="majorId" label="专业名字" min-width="220" align="center">
        <template #default="scope">{{ byIdGetName(scope.row.majorId, state.majorData) }}</template>
      </el-table-column>

      <el-table-column label="头像" width="100" align="center">
        <template #default="scope">
          <el-image class="table-td-thumb" :src="scope.row.image" />
        </template>
      </el-table-column>

      <el-table-column prop="address" label="上次登录地点" width="160" align="center" />
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="学号" prop="id">
        <el-input v-model="formData.id" placeholder="请输入学号" maxlength="10" show-word-limit :disabled="state.isDisabled" />
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
        <el-date-picker type="date" placeholder="请选择日期" v-model="formData.birthday" format="YYYY-MM-DD" value-format="YYYY-MM-DD" style="width: 100%"> </el-date-picker>
      </el-form-item>

      <el-form-item label="学生密码" prop="password">
        <el-input v-model="formData.password" :placeholder="state.addOrUpdate ? `默认密码为123456` : `设置新密码`" maxlength="20" show-password />
      </el-form-item>

      <el-form-item label="专业名字" prop="majorId">
        <el-select v-model="formData.majorId" placeholder="请选择专业" @change="getChange(formData.majorId)">
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
