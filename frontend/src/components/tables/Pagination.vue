<template>
  <!-- 分页 -->
  <div class="pagination">
    <el-pagination background :page-size="pageSize" :total="!disabled ? pageTotal : pageIndex"
      :current-page="pageIndex" :layout="layout" :disabled="disabled"
      @current-change="handlePageChange" />
  </div>
</template>

<script setup>
import { ref, toRefs } from 'vue';

const pageIndex = ref(1); // 当前页

const props = defineProps({
  pageSize: Number, //每页个数
  pageTotal: Number, // 总个数
  layout: {
    type: String,
    default: 'total, prev, pager, next, jumper',
  }, // 布局
  disabled: Boolean, // 是否显示分页
});

const { pageSize, pageTotal, layout, disabled } = toRefs(props);

const emit = defineEmits(['pageIndex']);

/**
 * 分页导航
 */
function handlePageChange(val) {
  pageIndex.value = val;
  emit('pageIndex', pageIndex.value);
}

defineExpose({
  pageSize,
  pageTotal,
  layout,
  disabled,
  handlePageChange,
});
</script>