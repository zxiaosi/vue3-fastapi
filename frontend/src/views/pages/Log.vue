<script setup lang="ts">
import { getLogs } from "@/apis";
import { onMounted, reactive } from "vue";
import MyTable from "@/components/MyTable.vue";

const state = reactive({
  tableData: {
    page: 1,
    page_size: 10,
    list: [] as any,
    total: 0,
  },
});

const columnOptions = [
  { prop: "id", label: "Id" },
  { prop: "url", label: "请求Url" },
  { prop: "ip", label: "请求ip" },
  { prop: "params", label: "请求参数" },
  { prop: "spend_time", label: "响应时间" },
  { prop: "create_time", label: "创建时间" },
];

onMounted(async () => {
  requestList({ page: 1, page_size: 10 });
});

const requestList = async (params: any) => {
  const { page, page_size } = params;
  const { data: { data, total }} = await getLogs({ ...params });
  state.tableData = { list: data, total: total, page, page_size };
};

const handlePageChange = (value: number) => {
  requestList({ page: value, page_size: state.tableData.page_size });
};
</script>

<template>
  <MyTable
    :columns="columnOptions"
    :data-source="state.tableData.list"
    :page="state.tableData.page"
    :page-size="state.tableData.page_size"
    :total="state.tableData.total"
    :on-page-change="handlePageChange"
  />
</template>

<style scoped lang="less"></style>
