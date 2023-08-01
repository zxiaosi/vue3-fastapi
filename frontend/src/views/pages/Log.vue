<script setup lang="tsx">
import { getLogs } from "@/apis";
import { onMounted, ref } from "vue";
import MyTableV2 from "@/components/MyTableV2.vue";
import type { Column } from "element-plus";

const tableData = ref({
  page: 1,
  page_size: 10,
  list: [] as any,
  total: 0,
});

/** 渲染响应时间 */
const renderTime = ({ cellData }: any) => {
  return <div>{Number(cellData).toFixed(4)}ms</div>;
};

const columnOptions: Column[] = [
  { key: "id", dataKey: "id", title: "Id", align: "center", width: 80 },
  { key: "url", dataKey: "url", title: "请求Url", align: "center", width: 200 },
  { key: "ip", dataKey: "ip", title: "请求ip", align: "center", width: 160 },
  { key: "params", dataKey: "params", title: "请求参数", align: "center", width: 400, flexGrow: 1 },
  {
    key: "spend_time",
    dataKey: "spend_time",
    title: "响应时间",
    align: "center",
    width: 120,
    cellRenderer: (record: any) => renderTime(record),
  },
  { key: "create_time", dataKey: "create_time", title: "创建时间", align: "center", width: 200 },
] as any;

onMounted(async () => {
  requestList({ page: 1, page_size: tableData.value.page_size });
});

/** 请求表格数据 */
const requestList = async (params: any) => {
  const { page, page_size } = params;
  const {
    data: { data, total },
  } = await getLogs({ ...params });
  tableData.value = { list: data, total: total, page, page_size };
};

/** 分页变化时触发 */
const handlePageChange = (value: number) => {
  requestList({ page: value, page_size: tableData.value.page_size });
};

/** 每页个数发生变化时触发 */
const handleSizeChange = (value: number) => {
  requestList({ page: tableData.value.page, page_size: value });
};
</script>

<template>
  <MyTableV2
    :columns="columnOptions"
    :data-source="tableData.list"
    :page="tableData.page"
    :page-size="tableData.page_size"
    :total="tableData.total"
    :on-page-change="handlePageChange"
    :on-size-change="handleSizeChange"
  />
</template>

<style scoped lang="less"></style>
