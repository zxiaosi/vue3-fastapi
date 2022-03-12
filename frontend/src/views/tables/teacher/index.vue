<script setup lang="ts">
import { reactive, onMounted } from "vue";
import { useDataStore } from "@/stores/data";
import BaseTable from "@/components/baseTable/index.vue";
import { read_datas, read_datas_relation } from "@/api";
import { pathEnum, type queryType, type teachFormType } from "@/types/table";
import type { stateType, enumType } from ".";
import { valueList, byIdGetName } from "@/utils/handleArray";

// 状态管理
const dataStore = useDataStore();

// 变量
const state: stateType = reactive({
  teacherData: [], // 教师表数据
  deptData: [], // 院系表数据
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

// 学历枚举
const eduEnum: enumType = {
  "1": { tag: "", name: "学士" },
  "2": { tag: "success", name: "硕士" },
  "3": { tag: "warning", name: "博士" },
};

// 职称枚举
const titleEnum: enumType = {
  "1": { tag: "", name: "助教" },
  "2": { tag: "success", name: "讲师" },
  "3": { tag: "warning", name: "副教授" },
  "4": { tag: "danger", name: "教授" },
};

// 表单对象
const formData: teachFormType = reactive({
  id: "",
  name: "",
  sex: "0",
  birthday: "",
  education: "1",
  title: "1",
  address: "",
  image: "",
  password: "123456",
  department_id: "",
});

// 定义校验规则
const formRules = reactive({
  id: [
    { required: "true", trigger: "change", message: "请输入职工号" },
    { pattern: /^[1-9]/, message: "职工号不能以0开头" },
    { min: 6, max: 6, message: "职工号的长度应为6" },
    { pattern: /^[1-9][0-9]{5}$/, message: "职工号必须是正整数" },
    {
      validator: (rule: any, value: string, callback: any) => {
        let idList = valueList(dataStore.teacherData, "id");
        if (!state.isDisabled && idList.indexOf(value) != -1) {
          callback(new Error("院系编号已经存在"));
        } else {
          callback(); // 验证通过
        }
      },
    },
  ],
  name: [
    { required: "true", message: "请输入教师名称(最大长度为10)", trigger: ["change", "blur"] },
    {
      validator: (rule: any, value: string, callback: any) => {
        let nameList = valueList(dataStore.teacherData, "name");
        if (!state.isDisabled && nameList.indexOf(value) != -1) {
          callback(new Error("院系名字已经存在"));
        } else {
          callback(); // 验证通过
        }
      },
    },
  ],
  sex: [{ required: "true", message: "请输入教师性别", trigger: "change" }],
  birthday: [{ required: "true", message: "请选择生日", trigger: "change" }],
  password: [{ message: "请输入新密码", trigger: "change" }],
  education: [{ required: "true", message: "请选择教师学历", trigger: "change" }],
  title: [{ required: "true", message: "请选择教师职称", trigger: "change" }],
  department_id: [{ required: "true", message: "请选择院系", trigger: "change" }],
});

/**
 * 获取表格数据
 */
const getData = async (currentPage: number = query.currentPage) => {
  // 获取教师表数据
  let params = { path: pathEnum.teacher, pageIndex: currentPage, pageSize: query.pageSize };
  const { data: teacherData } = await read_datas(params);
  state.teacherData = teacherData.dataList;
  state.pageTotal = teacherData.count;

  // 获取院系信息
  const { data: deptData } = await read_datas_relation("department");
  state.deptData = deptData;
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
    :data="state.teacherData"
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
        label="职工号"
        width="120"
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

      <el-table-column prop="education" label="学历" width="80" align="center">
        <template #default="scope">
          <el-tag :type="eduEnum[scope.row.education].tag">
            {{ eduEnum[scope.row.education].name }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column prop="title" label="职称" width="100" align="center">
        <template #default="scope">
          <el-tag :type="titleEnum[scope.row.title].tag">
            {{ titleEnum[scope.row.title].name }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column label="头像" width="100" align="center">
        <template #default="scope">
          <el-image class="table-td-thumb" :src="scope.row.image" />
        </template>
      </el-table-column>

      <el-table-column prop="address" label="上次登录地点" width="160" align="center" />

      <el-table-column prop="department_id" label="院系名字" width="180" align="center">
        <template #default="scope">{{ byIdGetName(scope.row.department_id, state.deptData) }}</template>
      </el-table-column>
    </template>

    <!-- 弹出框内容 -->
    <template #showDialog>
      <el-form-item label="职工号" prop="id">
        <el-input
          v-model="formData.id"
          placeholder="请输入职工号"
          maxlength="6"
          show-word-limit
          :disabled="state.isDisabled"
        />
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
        <el-date-picker
          type="date"
          placeholder="请选择日期"
          v-model="formData.birthday"
          format="YYYY-MM-DD"
          value-format="YYYY-MM-DD"
          style="width: 100%"
        />
      </el-form-item>

      <el-form-item label="教师密码" prop="password">
        <el-input
          v-model="formData.password"
          :placeholder="state.addOrUpdate == true ? `默认密码为123456` : `设置新密码`"
          maxlength="20"
          show-password
        />
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

.table-td-thumb {
  display: block;
  margin: auto;
  width: 35px;
  height: 35px;
}
</style>
