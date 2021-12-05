<template>
  <!-- 分页 -->
  <div class="pagination">
    <el-pagination background :page-size="pagesize" :total="pageTotal" :page-sizes="[10]"
      :current-page="pageIndex" @size-change="handleSizeChange" @current-change="handlePageChange"
      :layout="layout" />
  </div>
</template>

<script setup>
import { ref, toRefs } from 'vue';
import { defineProps } from '@vue/runtime-core';
const props = defineProps({
  pagesize: Number, //一页多少条
  pageTotal: Number, // 总个数
  layout: {
    type: String,
    default: 'total, sizes, prev, pager, next, jumper',
  }, // 布局
  render: Function, // 跳转触发的请求
});

const pageIndex = ref(1); // 当前页
const { pagesize, pageTotal, layout } = toRefs(props);

// 切换分页条数(未生效)
const handleSizeChange = (val) => {
  console.log(`每页 ${val} 条`);
};

const emit = defineEmits(['pageIndex']);

// 分页导航
const handlePageChange = (val) => {
  console.log(`当前页: ${val}`);
  pageIndex.value = val;
  props.render();
  emit('pageIndex', pageIndex.value);
};

defineExpose({
  pageIndex,
  pagesize,
  pageTotal,
  layout,
  handleSizeChange,
  handlePageChange,
});
</script>