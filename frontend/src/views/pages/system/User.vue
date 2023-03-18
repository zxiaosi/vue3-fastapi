<script setup lang="ts">
import { getUsers } from "@/apis";
import { onMounted, reactive, ref } from "vue";

const tableData = reactive({
  list: [] as any,
  total: 0,
});

onMounted(async () => {
  const { data: { data, total } } = await getUsers();
  tableData.list = data;
  tableData.total = total;
});
</script>

<template>
  <div class="page">
    <div class="header"> 搜索条件 </div>
    <el-table :data="tableData.list" stripe :border="true">
      <el-table-column prop="id" label="Id" />
      <el-table-column prop="name" label="Name" />
      <el-table-column prop="sex" label="Sex" />
      <el-table-column prop="avatar" label="avatar" />
      <el-table-column prop="phone" label="phone" />
      <el-table-column prop="create_time" label="create_time" />
      <el-table-column prop="update_time" label="update_time" />
    </el-table>
    <el-pagination background layout="total, sizes, prev, pager, next, jumper" :total="tableData.total" />
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
