<script lang="ts" setup>
import { computed, onBeforeMount, onMounted, reactive } from "vue";
import Breadcrumb from "@/components/breadcrumb/index.vue";
import { getSpanMethod } from "@/utils/spanMethod";
import { getElectiveDetail } from "@/api";
import { PathEnum } from "@/types/table";
import type { State, Data } from ".";
import { getLocal } from "@/request/auth";
import { dateFunction } from "@/utils/handleTime";

const state: State = reactive({
  dataList: [],
});

onBeforeMount(async () => {
  await getData();
});

const getData = async () => {
  const { data } = await getElectiveDetail({ path: PathEnum.elective });
  state.dataList = processData(data);
};

const processData = (data: Data[]) => {
  let userInfo = JSON.parse(getLocal("userInfo"));
  data.map((item) => {
    item.name = userInfo.name;
    item.teacherName = item.teacherName || "无";
    item.create_time = dateFunction(item.create_time);
  });
  return data;
};

const spanMethod = computed(() => {
  return getSpanMethod(state.dataList, ["name", "teacherName"], []);
});
</script>

<template>
  <div>
    <!-- 面包屑 -->
    <breadcrumb />

    <div class="container">
      <el-table :data="state.dataList" :span-method="spanMethod" border style="width: 100%">
        <el-table-column prop="name" label="姓名" min-width="160" align="center" />
        <el-table-column prop="teacherName" label="教师" min-width="160" align="center" />
        <el-table-column prop="courseName" label="课程" min-width="280" align="center" />
        <el-table-column prop="grade" label="成绩" min-width="140" align="center" />
        <el-table-column prop="create_time" label="选课时间" min-width="200" align="center" />
      </el-table>
    </div>
  </div>
</template>
