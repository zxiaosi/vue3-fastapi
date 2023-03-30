<script setup lang="ts">
/** 参考: https://blog.csdn.net/weixin_45291937/article/details/125523244 */

interface Columns {
  type?: "selection" | "index" | "expand"; // 多选框 | 索引 | 可展开
  prop?: string; // 列内容的字段名
  label?: string; // 显示的标题
  width?: string | number; // 对应列的宽度(不设置则按按比例)
  align?: "left" | "center" | "right"; // 对齐方式
  fixed?: "left" | "right"; // 固定在左侧或者右侧
  renderHeader?: ({ column, index }: any) => any; // 列标题 Label 区域渲染使用的 Function
  renderColumn?: ({ row, column, index }: any) => any; // 列 Column 区域渲染使用的 Function
}

interface Props {
  /** 表格配置 */
  columns: Columns[];
  dataSource: any[];

  /** 分页配置 */
  page?: number | any; // 当前页面 (加 any 防止下面 计算报错页数)
  pageSize?: number | any; // 每页显示条数 (加 any 防止下面 计算报错页数)
  total?: number; // 总条数 (如果total存在则显示分页器, 否则则不显示)
  onPageChange?: (page: number) => void; // 分页变化时触发
  onSizeChange?: (size: number) => void; // 每页个数发生变化时触发
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
          <template v-if="item.renderHeader" #header="{ column, $index }">
            <component :is="item.renderHeader" :column="column" :index="$index" />
          </template>

          <template v-if="item.renderColumn" #default="{ row, column, $index }">
            <component :is="item.renderColumn" :row="row" :column="column" :index="$index" />
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
        v-on:current-change="props?.onPageChange"
        v-on:size-change="props?.onSizeChange"
      >
        第 {{ (props.page - 1) * props.pageSize + 1 }}-{{ props.page * props.pageSize }} 条 / 共 {{ props.total }} 条
      </el-pagination>
    </template>
  </div>
</template>

<style scoped lang="less">
.mytable {
  .el-table {
    display: flex;
    flex: 1;
  }

  .el-pagination {
    padding-top: 20px;
    display: flex;
    justify-content: flex-end;
  }
}
</style>
