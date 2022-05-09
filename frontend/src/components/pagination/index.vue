<script setup lang="ts">
import { reactive } from "vue";

// 由上个页面传下来的数据, 不能写到其他页面
interface Props {
  currentPage: number; // 当前页码 G
  pageSize: number; // 每页个数
  pageTotal: number; // 总个数
  disabled: boolean; // 是否显示分页
}

const props = defineProps<Props>();

const state = reactive({
  pageIndex: props.currentPage as number, // 当前页码(不能直接修改props里面的值)
  layout: "->, total, prev, pager, next, jumper" as string, // 布局
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
