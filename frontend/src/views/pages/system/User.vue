<script setup lang="ts">
import { getUsers } from "@/apis";
import { h, onMounted, reactive, ref, render } from "vue";
import MyTable from "@/components/MyTable.vue";
import { ElTooltip, ElTag, ElIcon } from "element-plus";
import { Warning } from "@element-plus/icons-vue";
import { IMAGE_URL } from "@/assets/js/global";

const state = reactive({
  tableData: {
    page: 1,
    page_size: 10,
    list: [] as any,
    total: 0,
  },
});

/** 渲染手机号头 */
const renderPhone = ({ column, index }: any) => {
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
  const myTooltip = h(ElTooltip, { content: "手机号", placement: "top" }, { default: () => myIcon });
  return h("div", { style: { display: "flex", alignItems: "center", justifyContent: "center" } }, [myText, myTooltip]);
};

/** 渲染性别 */
const renderSex = ({ row, column, index }: any) => {
  // console.log(row, column, index);
  let sexOption = [
    { id: 0, key: "未知" },
    { id: 1, key: "男" },
    { id: 2, key: "女" },
  ];
  return sexOption.filter((item) => item.id == row.sex)[0]?.key;
};

const columnOptions = [
  { prop: "id", label: "Id", align: "center", width: 60 },
  { prop: "name", label: "姓名", align: "center", width: 160 },
  { prop: "sex", label: "性别", align: "center", width: 120, renderColumn: (record: any) => renderSex(record) },
  { prop: "avatar", label: "头像", align: "center", width: 120, slotColumn: true },
  {
    prop: "phone",
    label: "手机号",
    width: 200,
    align: "center",
    renderHeader: (record: any) => renderPhone(record),
  },
  {
    prop: "is_deleted",
    label: "状态",
    width: 140,
    align: "center",
    slotHeader: true,
    slotColumn: true,
  },
  { prop: "create_time", label: "创建时间", align: "center" },
  { prop: "update_time", label: "更新时间", align: "center" },
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
    >
      <!-- 头像列表插槽 -->
      <template #avatar_column="{ row, column, index }">
        <div class="avatar">
          <el-image
            v-if="row.avatar"
            :src="IMAGE_URL + row.avatar"
            :preview-src-list="[IMAGE_URL + row.avatar]"
            :preview-teleported="true"
            hide-on-click-modal
          />
          <el-image v-else src="https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg" />
        </div>
      </template>

      <!-- 状态头部插槽 -->
      <template #is_deleted_header="{ column, index }">
        <div class="status">
          <div>{{ column.label }}</div>
          <el-tooltip content="状态" placement="top">
            <el-icon>
              <Warning />
            </el-icon>
          </el-tooltip>
        </div>
      </template>

      <!-- 状态列表插槽 -->
      <template #is_deleted_column="{ row, column, index }">
        <el-tag :type="row.is_deleted == 0 ? 'success' : 'danger'">
          {{ row.is_deleted == 0 ? "正常" : "禁用" }}
        </el-tag>
      </template>
    </MyTable>
  </div>
</template>

<style scoped lang="less">
.page {
  .header {
    padding-bottom: 20px;
  }

  .avatar {
    display: flex;
    align-items: center;
    justify-content: center;

    .el-image {
      width: 30px;
      height: 30px;
      border-radius: 50%;
    }
  }
  .status {
    display: flex;
    align-items: center;
    justify-content: center;

    div {
      margin-right: 5px;
    }
  }
}
</style>
