<script setup lang="ts">
import { getUsers } from "@/apis";
import { onMounted, reactive, ref } from "vue";

const tableData = reactive({
  page: 1,
  page_size: 10,
  list: [] as any,
  total: 0,
});

onMounted(async () => {
  requestList({ page: 1, page_size: 10 })
});

const requestList = async (params: any) => {
  const { data: { data, total } } = await getUsers({ ...params });
  tableData.list = data;
  tableData.total = total;
}

const handlePageChange = (value: number) => {
  requestList({ page: value, page_size: tableData.page_size });
}
</script>

<template>
  <div class="page">
    <div class="header"> 搜索条件 </div>
    <el-table :data="tableData.list" stripe border>
      <el-table-column prop="id" label="Id" />
      <el-table-column prop="name" label="Name" />
      <el-table-column prop="sex" label="Sex" />
      <el-table-column prop="avatar" label="avatar" />
      <el-table-column prop="phone" label="phone" />
      <el-table-column prop="create_time" label="create_time" />
      <el-table-column prop="update_time" label="update_time" />
    </el-table>
    <el-pagination background layout="total, prev, pager, next, jumper" :total="tableData.total"
      v-model:current-page="tableData.page" v-model:page-size="tableData.page_size"
      v-on:current-change="handlePageChange" />
  </div>
</template>

<style scoped lang="less">
.page {
  .header {
    padding-bottom: 20px;
  }

  .el-table {
    flex: 1;
  }

  .el-pagination {
    padding-top: 20px;
    display: flex;
    justify-content: flex-end;
  }
}
</style>
