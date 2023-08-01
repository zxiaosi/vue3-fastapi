<script setup lang="tsx">
import { getRoles } from "@/apis";
import { onMounted, ref } from "vue";
import MyTableV2 from "@/components/MyTableV2.vue";
import type { Column } from "element-plus";

const tableData = ref({
  page: 1,
  page_size: 10,
  list: [],
  total: 0,
});

/** 渲染状态 */
const renderStatus = ({ cellData }: any) => {
  cellData = Boolean(1 - cellData);
  return <el-switch v-model={cellData} />;
};

const columnOptions: Column[] = [
  { key: "id", dataKey: "id", title: "Id", align: "center", width: 80 },
  { key: "name", dataKey: "name", title: "名称", align: "center", width: 160 },
  { key: "code", dataKey: "code", title: "Code", align: "center", width: 160 },
  { key: "description", dataKey: "description", title: "描述", align: "center", width: 200 },
  { key: "create_time", dataKey: "create_time", title: "创建时间", align: "center", width: 200, flexGrow: 1 },
  { key: "update_time", dataKey: "update_time", title: "更新时间", align: "center", width: 200, flexGrow: 1 },
  {
    key: "is_deleted",
    dataKey: "is_deleted",
    title: "状态",
    align: "center",
    width: 120,
    cellRenderer: (record) => renderStatus(record),
  },
];

onMounted(async () => {
  requestList({ page: 1, page_size: tableData.value.page_size });
});

/** 请求表格数据 */
const requestList = async (params: any) => {
  const { page, page_size } = params;
  const {
    data: { data, total },
  } = await getRoles({ ...params });
  tableData.value = { list: data, total, page, page_size };
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
  <div class="page">
    <div class="header">搜索条件</div>

    <MyTableV2
      :columns="columnOptions"
      :data-source="tableData.list"
      :page="tableData.page"
      :page-size="tableData.page_size"
      :total="tableData.total"
      :on-page-change="handlePageChange"
      :on-size-change="handleSizeChange"
    />
  </div>
</template>

<style scoped lang="less">
.page {
  .header {
    padding-bottom: 20px;
  }
}
</style>
