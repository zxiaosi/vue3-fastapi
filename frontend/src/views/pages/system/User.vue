<script setup lang="tsx">
import { getUsers } from "@/apis";
import { onMounted, ref } from "vue";
import MyTableV2 from "@/components/MyTableV2.vue";
import type { Column } from "element-plus";
import { Warning } from "@element-plus/icons-vue";
import { IMAGE_URL } from "@/assets/js/global";

// 表格数据
const tableData = ref({
  page: 1,
  page_size: 10,
  list: [],
  total: 0,
});

// 表格中状态数据
const switchData = ref({
  data: false,
  loading: false,
});

/** 渲染性别 */
const renderSex = ({ cellData }: any) => {
  const options = [
    { id: 0, key: "未知" },
    { id: 1, key: "男" },
    { id: 2, key: "女" },
  ];
  return <div>{options.filter((item) => item.id == cellData)[0]?.key}</div>;
};

/** 渲染用户头像 */
const renderAvatar = ({ cellData }: any) => {
  return (
    <div class={"user-view-avatar"}>
      {cellData ? (
        <el-image
          src={IMAGE_URL + cellData}
          preview-src-list={[IMAGE_URL + cellData]}
          preview-teleported="true"
          hide-on-click-modal
        />
      ) : (
        <el-image src="https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg" />
      )}
    </div>
  );
};

/** 渲染状态 */
const renderStatus = ({ cellData }: any) => {
  switchData.value.data = Boolean(1 - cellData);
  const { data, loading } = switchData.value;
  return <el-switch v-model={data} loading={loading} before-change={() => beforeChange()} />;
};

/** 渲染状态头部 */
const renderStatusHeader = ({ column: { title } }: any) => {
  return (
    <div class={"user-view-status"}>
      <div>{title}</div>
      <el-tooltip content="状态" placement="top">
        <el-icon>
          <Warning />
        </el-icon>
      </el-tooltip>
    </div>
  );
};

const columnOptions: Column[] = [
  { key: "id", dataKey: "id", title: "Id", align: "center", width: 80 },
  { key: "name", dataKey: "name", title: "姓名", align: "center", width: 160 },
  {
    key: "sex",
    dataKey: "sex",
    title: "性别",
    align: "center",
    width: 120,
    cellRenderer: (record) => renderSex(record),
  },
  {
    key: "avatar",
    dataKey: "avatar",
    title: "头像",
    align: "center",
    width: 120,
    cellRenderer: (record) => renderAvatar(record),
  },
  { key: "phone", dataKey: "phone", title: "手机号", align: "center", width: 200 },
  { key: "create_time", dataKey: "create_time", title: "创建时间", align: "center", width: 200, flexGrow: 1 },
  { key: "update_time", dataKey: "update_time", title: "更新时间", align: "center", width: 200, flexGrow: 1 },
  {
    key: "is_deleted",
    dataKey: "is_deleted",
    title: "状态",
    align: "center",
    width: 120,
    cellRenderer: (record) => renderStatus(record),
    headerCellRenderer: (record) => renderStatusHeader(record),
  },
];

onMounted(async () => {
  requestList({ page: 1, page_size: tableData.value.page_size });
});

/** 请求表格数据 */
const requestList = async (params: any) => {
  const { page, page_size } = params;
  const {
    data: { data, total },
  } = await getUsers({ ...params });
  tableData.value = { list: data, total, page, page_size };
};

/** 分页变化时触发 */
const handlePageChange = (value: number) => {
  requestList({ page: value, page_size: tableData.value.page_size });
};

/** 每页个数发生变化时触发 */
const handleSizeChange = (value: number) => {
  requestList({ page: tableData.value.page, page_size: value });
};

const beforeChange = () => {
  switchData.value.loading = true;
  // return new Promise((resolve) => {
  //   // setTimeout(() => {
  //   //   switchData.value.loading = false;
  //   //   ElMessage.success("Switch success");
  //   //   return resolve(true);
  //   // }, 1000);
  // });
};
</script>

<template>
  <div class="page">
    <div class="header">搜索条件</div>

    <MyTableV2
      :columns="columnOptions"
      :data-source="tableData.list"
      :page="tableData.page"
      :page-size="tableData.page_size"
      :total="tableData.total"
      :on-page-change="handlePageChange"
      :on-size-change="handleSizeChange"
    />
  </div>
</template>

<style scoped lang="less">
.page {
  .header {
    padding-bottom: 20px;
  }

  :deep(.user-view-avatar) {
    display: flex;
    align-items: center;
    justify-content: center;

    .el-image {
      width: 30px;
      height: 30px;
      border-radius: 50%;
    }
  }

  :deep(.user-view-status) {
    display: flex;
    align-items: center;
    justify-content: center;

    .el-icon {
      margin-left: 5px;
    }
  }
}
</style>
