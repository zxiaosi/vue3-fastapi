<script lang="ts" setup>
import { computed, onBeforeMount, onMounted, reactive, ref } from "vue";
import { Operation } from "@element-plus/icons-vue";
import { ElMessage, type FormInstance, type FormRules } from "element-plus";
import Breadcrumb from "@/components/breadcrumb/index.vue";
import { getSpanMethod } from "@/utils/spanMethod";
import { getTughtDetail, updateData } from "@/api";
import { PathEnum } from "@/types/table";
import type { State, Data } from ".";
import { getLocal } from "@/request/auth";
import { dateFunction } from "@/utils/handleTime";

const state: State = reactive({
  dataList: [],
  showDialog: false, // 是否显示弹框
  electiveId: 0, // 选课id
});

// 表单的值
const formRef = ref<FormInstance>();

const formData = reactive({
  electiveId: 0,
  courseId: "",
  courseName: "",
  studentId: "",
  studentName: "",
  grade: "",
});

const formRules = reactive<FormRules>({
  grade: [{ pattern: /(^\s{0}$)|(^100)|(^([0]{0})([1-9]?)([0-9]))$/, message: "请输入正确的成绩分数" }],
});

onBeforeMount(async () => {
  await getData();
});

const spanMethod = computed(() => {
  return getSpanMethod(state.dataList, ["name", "courseName", "studentName"], []);
});

const getData = async () => {
  const { data } = await getTughtDetail({ path: PathEnum.taught });
  state.dataList = processData(data);
};

const processData = (data: Data[]) => {
  let userInfo = JSON.parse(getLocal("userInfo"));
  data.map((item) => {
    item.name = userInfo.name;
    item.update_time = dateFunction(item.update_time);
  });
  return data;
};

/**
 * 编辑信息
 */
const handleEdit = (row: any) => {
  Object.keys(formData).forEach((item) => {
    formData[item] = row[item];
  });

  // 显示更新弹窗
  state.showDialog = true;

  state.electiveId = row.id; // 选课id
};

/**
 * 确认更新
 */
const saveEdit = (formEl: FormInstance | undefined) => {
  state.showDialog = false;

  if (!formEl) return;
  formEl.validate(async (valid: any) => {
    if (valid) {
      let params = { path: PathEnum.elective, id: state.electiveId, studentId: formData.studentId, courseId: formData.courseId, grade: formData.grade };
      const tmp = await updateData(params);
      ElMessage.success(`成功修改学生的成绩！`);
      await getData();
    } else {
      ElMessage.warning("数据不符合校验规则，添加失败！");
    }
  });
};
</script>

<template>
  <div>
    <!-- 面包屑 -->
    <breadcrumb />

    <div class="container">
      <el-table :data="state.dataList" :span-method="spanMethod" border style="width: 100%">
        <el-table-column prop="name" label="姓名" min-width="160" align="center" />
        <el-table-column prop="courseName" label="课程" min-width="160" align="center" />
        <el-table-column prop="studentName" label="学生" min-width="280" align="center" />
        <el-table-column prop="grade" label="成绩" min-width="140" align="center" />
        <el-table-column prop="update_time" label="更新时间" min-width="200" align="center" />

        <el-table-column label="操作" min-width="180" align="center" fixed="right">
          <template #default="scope">
            <el-button size="small" type="primary" :icon="Operation" @click="handleEdit(scope.row)">修改成绩</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <!-- 更新弹窗 -->
    <el-dialog title="修改成绩" v-model="state.showDialog" width="22%" draggable>
      <el-form :model="formData" :rules="formRules" ref="formRef" label-width="100px">
        <el-form-item label="课程" prop="courseId">
          <el-input v-model="formData.courseName" disabled />
        </el-form-item>
        <el-form-item label="学生" prop="studentId">
          <el-input v-model="formData.studentName" disabled />
        </el-form-item>
        <el-form-item label="成绩" prop="grade">
          <el-input v-model="formData.grade" placeholder="请输入成绩(默认为0)"></el-input>
        </el-form-item>
      </el-form>

      <template #footer>
        <span class="dialog-footer">
          <el-button @click="state.showDialog = false">取 消</el-button>
          <el-button type="primary" @click="saveEdit(formRef)">更 新</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>
