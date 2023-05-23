<script setup lang="tsx">
import type {
  Column,
  ExpandedRowsChangeHandler,
  HeaderClassNameGetter,
  RowClassNameGetter,
  RowExpandHandler,
} from "element-plus";
import { computed } from "vue";

interface Props {
  /** 表格列配置 */
  columns: Column<any>[];
  /** 表格数据源 */
  dataSource: any[];
  /** 列表长度 */
  dataLength?: number;
  /** 自定义类名 */
  className?: string;

  /** 当前页面 (加 any 防止下面 计算报错页数) */
  page?: number | any;
  /** 每页显示条数 (加 any 防止下面 计算报错页数) */
  pageSize?: number | any;
  /** 总条数 (如果total存在则显示分页器, 否则则不显示) */
  total?: number;
  /** 分页变化时触发 */
  onPageChange?: (page: number) => void;
  /** 每页个数发生变化时触发 */
  onSizeChange?: (size: number) => void;

  /** 树形数据 -- 列的 key 来标记哪个行可以被展开 */
  expandColumnKey?: string;
  /** 树形数据 -- 存放行展开状态的 key 的数组 */
  expandedRowKeys?: Array<string | number | symbol>;
  /** 树形数据 -- 点击箭头图标展开/折叠树节点时触发 */
  onRowExpanded?: (row: Parameters<RowExpandHandler>[0]) => void;
  /** 树形数据 -- 行展开状态改变时触发 */
  onExpandedRowsChange?: (expandedKeys: Parameters<ExpandedRowsChangeHandler>[0]) => void;
}

const props = withDefaults(defineProps<Props>(), {});

/** 表格高度 */
const tableHeight = computed(() => {
  const length = props.dataLength || props.dataSource.length;
  return length > 0 ? length * 50 + 50 : 344;
});

/** header 部分的自定义 class 名 */
const headerClass = (param: Parameters<HeaderClassNameGetter<any>>) => "table-header-bg";

/** row wrapper 部分的自定义 class 名 */
const rowClass = ({ rowIndex }: Parameters<RowClassNameGetter<any>>[0]) => {
  if (rowIndex % 2 === 1) {
    return "table-row-bg";
  } else {
    return "";
  }
};
</script>

<template>
  <div class="myTable">
    <div :class="className">
      <el-auto-resizer>
        <template #default="{ height, width }">
          <el-table-v2
            :columns="columns"
            :data="dataSource"
            :header-class="headerClass"
            :row-class="rowClass"
            :width="width"
            :height="tableHeight || height"
            :expand-column-key="expandColumnKey"
            :expanded-row-keys="expandedRowKeys"
            @row-expand="props?.onRowExpanded"
            @expanded-rows-change="props?.onExpandedRowsChange"
          />
        </template>
      </el-auto-resizer>
    </div>

    <template v-if="props.total">
      <el-pagination
        background
        layout="slot, prev, pager, next, sizes, jumper"
        :total="total"
        :current-page="page"
        :page-size="pageSize"
        @current-change="props.onPageChange"
        @size-change="props.onSizeChange"
      >
        第 {{ (page - 1) * pageSize + 1 }}-{{ page * pageSize }} 条 / 共 {{ total }} 条
      </el-pagination>
    </template>
  </div>
</template>

<style scoped lang="less">
.myTable {
  .el-table-v2 {
    // min-height: 344px; // 空列表时, 保证表格高度
  }

  .el-pagination {
    padding-top: 20px;
    display: flex;
    justify-content: flex-end;
  }

  // 表格头背景色(header-cell不生效)
  :deep(.table-header-bg) {
    background-color: #e5eefd;
  }

  // 表格头中 header-cell 背景色
  :deep(.el-table-v2__header-cell) {
    background-color: #e5eefd;
    border-right: 1px solid #dcdfe6;
  }

  // 表格行背景色
  :deep(.table-row-bg) {
    background-color: #e5eefd;
  }

  // 表格行 hover 时背景色
  :deep(.table-row-bg:hover) {
    background-color: var(--el-table-row-hover-bg-color);
  }
}
</style>
