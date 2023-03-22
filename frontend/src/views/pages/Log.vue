<script setup lang='ts'>
import { getLogs } from '@/apis';
import { onMounted, reactive } from 'vue';

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
  const { data: { data, total } } = await getLogs({ ...params });
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
      <el-table-column prop="url" label="请求Url" />
      <el-table-column prop="ip" label="请求ip" />
      <el-table-column prop="params" label="请求参数" />
      <el-table-column prop="spend_time" label="响应时间" />
      <el-table-column prop="create_time" label="创建时间" />
    </el-table>
    <el-pagination background layout="total, prev, pager, next, jumper" :total="tableData.total"
      v-model:current-page="tableData.page" v-model:page-size="tableData.page_size" v-on:current-change="handlePageChange" />
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