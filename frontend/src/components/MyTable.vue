<script setup lang="ts">
/** 参考: https://blog.csdn.net/weixin_45291937/article/details/125523244 */

interface Columns {
  /** 多选框 | 索引 | 可展开 */
  type?: "selection" | "index" | "expand";
  /** 列内容的字段名 */
  prop: string;
  /** 显示的标题 */
  label?: string;
  /** 对应列的宽度(不设置则按按比例) */
  width?: string | number;
  /** 对齐方式 */
  align?: "left" | "center" | "right";
  /** 固定在左侧或者右侧 */
  fixed?: "left" | "right";
  /** 列表插槽 Label */
  slotHeader?: boolean | string;
  /** 列表插槽列 Column */
  slotColumn?: boolean | string;
  /** 列表 Label 区域渲染使用的 Function */
  renderHeader?: ({ column, index }: any) => any;
  /** 列表 Column 区域渲染使用的 Function */
  renderColumn?: ({ row, column, index }: any) => any;
}

interface Props {
  /** 表格列配置 */
  columns: Columns[];
  /** 表格数据源 */
  dataSource: any[];

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
}

const props = withDefaults(defineProps<Props>(), {});
</script>

<template>
  <div class="mytable">
    <el-table :data="dataSource" stripe :border="true">
      <template v-for="item in props.columns">
        <el-table-column
          :type="item.type"
          :prop="item.prop"
          :label="item.label"
          :width="item.width"
          :align="item.align"
          :fixed="item.fixed"
          show-overflow-tooltip
        >
          <template #header="{ column, $index }">
            <!-- 插槽方式 (写在 <MyTable></MyTable> 标签里面) -->
            <slot
              v-if="item.slotHeader"
              :name="(item.slotHeader != true && item.slotHeader) || item.prop + '_header'"
              :column="column"
              :index="$index"
            ></slot>

            <!-- 组件方式 (返回 值 或者 h()) -->
            <component v-else-if="item.renderHeader" :is="item.renderHeader" :column="column" :index="$index" />

            <!-- 默认展示方式 -->
            <div v-else :style="{ textAlign: item.align }">{{ column.label }}</div>
          </template>

          <template #default="{ row, column, $index }">
            <!-- 插槽方式 (写在 <MyTable></MyTable> 标签里面) -->
            <slot
              v-if="item.slotColumn"
              :name="(item.slotColumn != true && item.slotColumn) || item.prop + '_column'"
              :row="row"
              :column="column"
              :index="$index"
            ></slot>

            <!-- 组件方式 (返回 值 或者 h()) -->
            <component
              v-else-if="item.renderColumn"
              :is="item.renderColumn"
              :row="row"
              :column="column"
              :index="$index"
            />

            <!-- 默认展示方式 (这里可不写, 用默认就好) -->
            <!-- <div v-else :style="{ textAlign: item.align }">{{ row[item.prop] }}</div> -->
          </template>
        </el-table-column>
      </template>
    </el-table>

    <template v-if="props.total">
      <el-pagination
        background
        layout="slot, prev, pager, next, sizes, jumper"
        :total="props.total"
        :current-page="props.page"
        :page-size="props.pageSize"
        @current-change="props?.onPageChange"
        @size-change="props?.onSizeChange"
      >
        第 {{ (props.page - 1) * props.pageSize + 1 }}-{{ props.page * props.pageSize }} 条 / 共 {{ props.total }} 条
      </el-pagination>
    </template>
  </div>
</template>

<style scoped lang="less">
.mytable {
  .el-table {
    width: 100%;
  }

  .el-pagination {
    padding-top: 20px;
    display: flex;
    justify-content: flex-end;
  }
}
</style>
