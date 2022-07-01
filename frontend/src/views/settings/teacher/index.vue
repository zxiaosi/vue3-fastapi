<script setup lang="ts">
import { reactive, onBeforeMount } from "vue";
import { useDataStore } from "@/stores/data";
import type { FormRules } from "element-plus";
import BaseTable from "@/components/BaseTable/index.vue";
import { readDatas } from "@/api";
import { PathEnum, type Query, type TeacherForm } from "@/types/table";
import { type State, SexEnum, EduEnum, TitleEnum, TagEnum } from ".";
import { valueList, byIdGetName } from "@/utils/handleArray";

// 状态管理
const dataStore = useDataStore();

// 变量
const state: State = reactive({
  teacherData: [], // 教师表数据
  deptData: [], // 院系表数据
  pageTotal: 0, // 数据的总个数
  isDisabled: false, // 是否禁用编辑框id(可选)
  addOrUpdate: false, // 添加数据或更新数据
});

// 搜索和页码
const query: Query = reactive({
  id: "",
  currentPage: 1,
  pageSize: 10,
});

// 表单对象
const formData: TeacherForm = reactive({
  id: "",
  name: "",
  sex: "0",
  birthday: "",
  education: "1",
  title: "1",
  address: "",
  image: "",
  password: "123456",
  departmentId: "",
});

/**
 * 对id进行验证
 */
const idValidate = (rule: any, value: string, callback: any) => {
  let idList = valueList(dataStore.teacherData, "id");
  if (!state.isDisabled && idList.indexOf(value) != -1) {
    callback(new Error("职工号已经存在"));
  } else {
    callback(); // 验证通过
  }
};

/**
 * 对name进行验证
 */
const nameValidate = (rule: any, value: string, callback: any) => {
  let nameList = valueList(dataStore.teacherData, "name");
  if (!state.isDisabled && nameList.indexOf(value) != -1) {
    callback(new Error("教师名字已经存在"));
  } else {
    callback(); // 验证通过
  }
};

// 定义校验规则
const formRules = reactive<FormRules>({
  id: [
    { required: true, trigger: "change", message: "请输入职工号" },
    { pattern: /^[1-9]/, message: "职工号不能以0开头" },
    { pattern: /^[1-9][0-9]{5}$/, message: "职工号必须是正整数且长度应为6" },
    { validator: idValidate },
  ],
  name: [{ required: true, message: "请输入教师名称(最大长度为10)", trigger: ["change", "blur"] }, { validator: nameValidate }],
  sex: [{ required: true, message: "请输入教师性别", trigger: "change" }],
  birthday: [{ required: true, message: "请选择生日", trigger: "change" }],
  password: [{ message: "请输入新密码", trigger: "change" }],
  education: [{ required: true, message: "请选择教师学历", trigger: "change" }],
  title: [{ required: true, message: "请选择教师职称", trigger: "change" }],
  departmentId: [{ required: true, message: "请选择院系", trigger: "change" }],
});

/**
 * 获取表格数据
 */
const getData = async (currentPage: number = query.currentPage) => {
  let dept = readDatas({ path: PathEnum.dept, pageIndex: -1, pageSize: -1 }); // 获取院系信息
  let teacjer = readDatas({ path: PathEnum.teacher, pageIndex: currentPage, pageSize: query.pageSize }); // 获取教师表数据

  const [{ data: deptData }, { data: teacherData }] = await Promise.all([dept, teacjer]);

  state.teacherData = teacherData.list;
  state.pageTotal = teacherData.count;
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
    :data="state.teacherData"
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
      <el-table-column prop="id" label="职工号" width="100" align="center" />
      <el-table-column prop="name" label="名字" width="120" align="center" />

      <el-table-column prop="sex" label="性别" width="80" align="center">
        <template #default="scope">
          <el-tag :type="TagEnum[scope.row.sex]">
            {{ SexEnum[scope.row.sex] }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column prop="birthday" label="生日" width="120" align="center" />

      <el-table-column prop="education" label="学历" width="80" align="center">
        <template #default="scope">
          <el-tag :type="TagEnum[scope.row.education - 1]">
            {{ EduEnum[scope.row.education - 1] }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column prop="title" label="职称" width="100" align="center">
        <template #default="scope">
          <el-tag :type="TagEnum[scope.row.title - 1]">
            {{ TitleEnum[scope.row.title - 1] }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column prop="departmentId" label="院系名字" width="180" align="center">
        <template #default="scope">{{ byIdGetName(scope.row.departmentId, state.deptData) }}</template>
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
      <el-form-item label="职工号" prop="id">
        <el-input v-model="formData.id" placeholder="请输入职工号" maxlength="6" show-word-limit :disabled="state.isDisabled" />
      </el-form-item>
      <el-form-item label="教师名字" prop="name">
        <el-input v-model="formData.name" placeholder="请输入名字" maxlength="10" show-word-limit />
      </el-form-item>

      <el-form-item label="教师性别" prop="sex">
        <el-select v-model="formData.sex" placeholder="请选择性别">
          <el-option key="1" label="男" value="0" />
          <el-option key="2" label="女" value="1" />
        </el-select>
      </el-form-item>

      <el-form-item label="教师生日" prop="birthday">
        <el-date-picker type="date" placeholder="请选择日期" v-model="formData.birthday" format="YYYY-MM-DD" value-format="YYYY-MM-DD" style="width: 100%" />
      </el-form-item>

      <el-form-item label="教师密码" prop="password">
        <el-input v-model="formData.password" :placeholder="state.addOrUpdate == true ? `默认密码为123456` : `设置新密码`" maxlength="20" show-password />
      </el-form-item>

      <el-form-item label="教师学历" prop="education">
        <el-select v-model="formData.education" placeholder="请选择学历">
          <el-option key="1" label="学士" value="1" />
          <el-option key="2" label="硕士" value="2" />
          <el-option key="3" label="博士" value="3" />
        </el-select>
      </el-form-item>

      <el-form-item label="教师职称" prop="title">
        <el-select v-model="formData.title" placeholder="请选择职称">
          <el-option key="1" label="助教" value="1" />
          <el-option key="2" label="讲师" value="2" />
          <el-option key="3" label="副教授" value="3" />
          <el-option key="4" label="教授" value="4" />
        </el-select>
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

.table-td-thumb {
  display: block;
  margin: auto;
  width: 35px;
  height: 35px;
}
</style>
