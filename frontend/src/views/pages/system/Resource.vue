<script setup lang="tsx">
import { getResources } from "@/apis";
import { computed, onMounted, ref } from "vue";
import MyTableV2 from "@/components/MyTableV2.vue";
import type { ExpandedRowsChangeHandler, RowExpandHandler, Column } from "element-plus";
import { arrayToTree } from "@/utils/handle_data";

/** 表格数据 */
const tableData = ref({
  expandedRowKeys: [] as string[],
  list: [],
  length: 0,
});

/** 树形数据 */
const treeData = computed(() => arrayToTree(tableData.value.list));

/** 渲染层级 */
const renderLevel = ({ cellData }: any) => {
  const options = [
    { id: 0, type: "", text: "目录" },
    { id: 1, type: "success", text: "菜单" },
    { id: 1, type: "warning", text: "权限" },
  ];
  return <el-tag type={options[cellData].type}>{options[cellData].text}</el-tag>;
};

/** 渲染状态 */
const renderStatus = ({ cellData }: any) => {
  cellData = Boolean(1 - cellData);
  return <el-switch v-model={cellData} />;
};

const columnOptions: Column[] = [
  { key: "name", dataKey: "name", title: "名称", align: "center", width: 160 },
  {
    key: "level",
    dataKey: "level",
    title: "层级",
    align: "center",
    width: 120,
    cellRenderer: (record) => renderLevel(record),
  },
  { key: "menu_url", dataKey: "menu_url", title: "路径", align: "center", width: 200 },
  { key: "permission_code", dataKey: "permission_code", title: "Code", align: "center", width: 200 },
  { key: "create_time", dataKey: "create_time", title: "创建时间", align: "center", width: 200, flexGrow: 1 },
  { key: "update_time", dataKey: "update_time", title: "更新时间", align: "center", width: 200, flexGrow: 1 },
  {
    key: "is_deleted",
    dataKey: "is_deleted",
    title: "状态",
    align: "center",
    width: 120,
    cellRenderer: (record) => renderStatus(record),
  },
];

onMounted(async () => {
  requestList();
});

/** 请求表格数据 */
const requestList = async () => {
  const {
    data: { data },
  } = await getResources();
  tableData.value = { ...tableData.value, list: data };
};

/** 点击箭头图标展开/折叠树节点时触发 */
const handleRowExpanded = (row: Parameters<RowExpandHandler>[0]) => {
  console.log("handleRowExpanded", row);
};

/** 行展开状态改变时触发 */
const handleExpandedRowsChange = (keys: Parameters<ExpandedRowsChangeHandler>[0]) => {
  let length = treeData.value?.length;
  keys.map((item: any) => {
    tableData.value.list.map((subItem: any) => {
      subItem.pid == item && (length += 1);
    });
  });
  tableData.value.length = length;
};
</script>

<template>
  <div class="page">
    <MyTableV2
      :columns="columnOptions"
      :data-source="treeData"
      :data-length="tableData.length"
      :expand-column-key="'name'"
      :expanded-row-keys="tableData.expandedRowKeys"
      @row-expanded="handleRowExpanded"
      @expanded-rows-change="handleExpandedRowsChange"
    />
  </div>
</template>

<style scoped lang="less">
.page {
}
</style>
