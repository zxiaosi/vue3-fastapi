<script setup lang="ts">
import { reactive } from "vue";
import type { stateType } from ".";

// 此处接口不能写到其他页面
interface propsType {
  currentPage: number; // 当前页码
  pageSize: number; // 每页个数
  pageTotal: number; // 总个数
  disabled: boolean; // 是否显示分页
}

const props = defineProps<propsType>();

const state: stateType = reactive({
  pageIndex: props.currentPage, // 当前页码(不能直接修改props里面的值)
  layout: "->, total, prev, pager, next, jumper", // 布局
});

const emit = defineEmits<{
  (e: "pageIndex", pageIndex: number): void;
}>();

/**
 * 分页导航
 */
const handlePageChange = (val: number) => {
  state.pageIndex = val;
  emit("pageIndex", state.pageIndex);
};
</script>

<template>
  <!-- 分页器 -->
  <div class="pagination">
    <el-pagination
      background
      :page-size="props.pageSize"
      :total="props.disabled ? props.pageTotal : state.pageIndex"
      :current-page="state.pageIndex"
      :layout="state.layout"
      :disabled="!props.disabled"
      @current-change="handlePageChange"
    />
  </div>
</template>
