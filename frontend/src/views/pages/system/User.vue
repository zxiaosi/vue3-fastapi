<script setup lang="ts">
import { getUsers } from "@/apis";
import { h, onMounted, reactive, ref, render } from "vue";
import MyTable from "@/components/MyTable.vue";
import { ElTooltip, ElTag, ElIcon } from "element-plus";
import { Warning } from "@element-plus/icons-vue";

const state = reactive({
  tableData: {
    page: 1,
    page_size: 10,
    list: [] as any,
    total: 0,
  },
});

/** 渲染手机号头 */
const renderPhoneHeader = ({ column, index }: any) => {
  // console.log(column, index);

  /**
   *
   * <div style="display: flex, align-items: center, justify-content: center">
   *   <div style="margin-right: "5px"">手机号</div>
   *   <el-tooltip content="测试" placement="top">
   *     <el-icon>
   *       <Warning />
   *     </el-icon>
   *   </el-tooltip>
   * </div>
   *
   */
  const myText = h("div", { style: { marginRight: "5px" } }, "手机号");
  const myIcon = h(ElIcon, null, { default: () => h(Warning) });
  const myTooltip = h(ElTooltip, { content: "测试", placement: "top" }, { default: () => myIcon });
  return h("div", { style: { display: "flex", alignItems: "center", justifyContent: "center" } }, [myText, myTooltip]);
};

/** 渲染状态 */
const renderStatus = ({ row, column, index }: any) => {
  // console.log(row, column, index);
  if (row.is_deleted == 0) return h(ElTag, { type: "success" }, { default: () => "正常" });
  else return h(ElTag, { type: "danger" }, { default: () => "禁用" });
};

const columnOptions = [
  { prop: "id", label: "Id", width: 40 },
  { prop: "name", label: "姓名", width: 120 },
  { prop: "sex", label: "性别", width: 120 },
  { prop: "avatar", label: "头像", width: 120 },
  { prop: "phone", label: "手机号", width: 120, renderHeader: (record: any) => renderPhoneHeader(record) },
  {
    prop: "is_deleted",
    label: "状态",
    width: 120,
    align: "center",
    renderColumn: (record: any) => renderStatus(record),
  },
  { prop: "create_time", label: "创建时间" },
  { prop: "update_time", label: "更新时间" },
] as any;

onMounted(async () => {
  requestList({ page: 1, page_size: 10 });
});

const requestList = async (params: any) => {
  const { page, page_size } = params;
  const {
    data: { data, total },
  } = await getUsers({ ...params });
  state.tableData = { list: data, total: total, page, page_size };
};

const handlePageChange = (value: number) => {
  requestList({ page: value, page_size: state.tableData.page_size });
};
</script>

<template>
  <div class="page">
    <div class="header">搜索条件</div>
    <MyTable
      :columns="columnOptions"
      :data-source="state.tableData.list"
      :page="state.tableData.page"
      :page-size="state.tableData.page_size"
      :total="state.tableData.total"
      :on-page-change="handlePageChange"
    />
  </div>
</template>

<style scoped lang="less">
.page {
  .header {
    padding-bottom: 20px;
  }
}
</style>
