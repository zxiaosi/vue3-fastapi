<script setup lang="ts">
import { ref, reactive, watch, watchEffect } from "vue";
import { useRoute } from "vue-router";
import { useDataStore } from "@/stores/data";
import { ElForm, ElMessage, ElMessageBox } from "element-plus";
import { Search, Remove, Delete, Plus, Edit } from "@element-plus/icons-vue";
import Breadcrumb from "../breadcrumb/index.vue";
import Pagination from "../pagination/index.vue";
import { read_data, delete_data, create_data, update_data, delete_datas, read_datas_relation } from "@/api";
import type { stateType } from ".";
import type { queryType, formDataType } from "@/types/table";
import { clickRecover } from "@/utils/clickRecover";

// 路由对象
const route = useRoute();

// 状态管理
const dataStore = useDataStore();

// 此处接口不能写到其他页面(父子传值)
interface propsType {
  query: queryType; // 搜索和页码
  data: formDataType[]; // 数据
  pageTotal: number; // 数据总个数
  formData: formDataType; // 表单对象
  formRules: object; // 校验规则
  getData: any; // 得到数据
}
const props = defineProps<propsType>();

// 变量
const state: stateType = reactive({
  pathParam: route.name, // 请求接口路径参数
  pageName: route.meta.title, // 页面名称
  searched: [], // 被搜索的数据(渲染表格数据需要是列表)
  isShowSearched: false, // 是否显示被搜索的数据
  selectedList: [], // 被勾选的列表
  relationData: [], // 依赖数据
  showDialog: false, // 是否显示弹窗
  addOrUpdate: true, // 是否是添加或更新(true-添加 | false-更新)
});

// 实例化表单
type FormInstance = InstanceType<typeof ElForm>;
const formRef = ref<FormInstance>();

const emit = defineEmits<{
  (e: "emitIsDisabled", isDisabled: boolean): void;
  (e: "emitIsShowSearched", isShowSearched: boolean): void;
  (e: "emitAddOrUpdate", addOrUpdate: boolean): void;
}>();

watchEffect(() => {
  // 是否显示被选择的值
  emit("emitIsShowSearched", state.isShowSearched);
  // 是否是添加或者更新
  emit("emitAddOrUpdate", state.addOrUpdate);
});

/**
 * 级联删除
 */
const cascadeDelete = () => {
  if (state.pathParam == "course" || state.pathParam == "selectCourse") {
    return "确定要删除吗？";
  } else {
    return "确定要删除吗？(以及相关联的数据)";
  }
};

/**
 * 搜索数据
 */
const handleSearch = async (event: any) => {
  clickRecover(event);

  let params = { path: state.pathParam, id: props.query.id };
  const { data } = await read_data(params);
  if (data) {
    state.isShowSearched = true;
    state.searched.splice(0, 1, data);
  }
};

/**
 * 移除搜索
 */
const handleRemove = (event: MouseEvent) => {
  clickRecover(event);
  removeSearch();
};

/**
 * 被勾选的数据
 */
const handleSelectionChange = (val: string[]) => {
  // 如果没有勾选,清空勾选列表
  if (val.length == 0) state.selectedList = [];

  val.forEach((item: any, index) => {
    state.selectedList.splice(index, 1, item.id);
  });
};

/**
 * 删除被勾选的数据
 */
const handleSelectedDelete = (event: MouseEvent) => {
  clickRecover(event);
  let text = cascadeDelete();

  // 二次确认删除
  ElMessageBox.confirm(text, "提示", {
    confirmButtonText: "删除",
    cancelButtonText: "取消",
    type: "warning",
  })
    .then(async () => {
      let params = { path: state.pathParam, idList: state.selectedList };
      await delete_datas(params);
      ElMessage.success(`成功删除 ${state.pageName} 中的数据！`);
      await removeSearch(true);
    })
    .catch(() => {});
};

/**
 * 获取依赖数据并存放到状态管理
 */
const getRelationData = async () => {
  const { data } = await read_datas_relation(state.pathParam);
  state.relationData = data.dataList;
  dataStore.handleData(state.pathParam, data.dataList);
};

/**
 * 添加数据按钮
 */
const handleAdd = async (event: MouseEvent) => {
  clickRecover(event);

  // 重置表单
  Object.keys(props.formData).forEach((key) => (props.formData[key] = ""));

  if (state.pathParam == "selectCourse") {
    props.formData["grade"] = "0";
  } else {
    await getRelationData();
  }

  // 显示添加弹窗
  state.showDialog = state.addOrUpdate = true;
  emit("emitIsDisabled", false);
};

/**
 * 确认添加
 */
const saveAdd = (formEl: FormInstance | undefined) => {
  state.showDialog = false;
  state.addOrUpdate = true;

  if (!formEl) return;
  formEl.validate(async (valid: any) => {
    if (valid) {
      let params = { path: state.pathParam, ...props.formData };
      await create_data(params);
      ElMessage.success(`成功添加编号为 ${props.formData.id} 的 ${state.pageName} 信息！`);
      await removeSearch(true);
    } else {
      ElMessage.warning("数据不符合校验规则，添加失败！");
    }

    // 重置表单
    formEl.resetFields();
  });
};

/**
 * 编辑院系信息
 */
const handleEdit = (row: any) => {
  Object.keys(props.formData).forEach((item) => {
    props.formData[item] = row[item];
  });

  // 显示更新弹窗
  state.showDialog = true;
  state.addOrUpdate = false;

  emit("emitIsDisabled", true);
};

/**
 * 确认更新
 */
const saveEdit = (formEl: FormInstance | undefined) => {
  state.showDialog = state.addOrUpdate = false;
  if (!formEl) return;
  formEl.validate(async (valid: any) => {
    if (valid) {
      let params = { path: state.pathParam, ...props.formData };
      await update_data(params);
      ElMessage.success(`成功修改ID为 ${props.formData.id} 的 ${state.pageName} 数据`);
      await removeSearch(true);
    } else {
      ElMessage.warning("数据不符合校验规则，添加失败！");
    }
  });
};

/**
 * 删除操作
 */
const handleDelete = (row: any) => {
  let text = cascadeDelete();

  // 二次确认删除
  ElMessageBox.confirm(text, "提示", {
    confirmButtonText: "删除",
    cancelButtonText: "取消",
    type: "warning",
  })
    .then(async () => {
      let params = { path: state.pathParam, id: row.id };
      await delete_data(params);
      ElMessage.success(`成功删除编号为 ${row.id} 的 ${state.pageName} 信息！`);
      await removeSearch(true);
    })
    .catch(() => {});
};

/**
 * 页面改变(子组件传值)
 */
const pageIndex = async (res: number) => {
  props.query.currentPage = res;
  await props.getData(res);
};

/**
 * 清除搜索
 */
const removeSearch = async (isNeedData: boolean = false) => {
  props.query.id = "";
  state.isShowSearched = false;
  if (isNeedData) {
    await props.getData();
  }
};
</script>

<template>
  <div>
    <!-- 面包屑 -->
    <breadcrumb />

    <!-- 表格 -->
    <div class="container">
      <!-- 搜索、清除搜索、多选删除、添加 -->
      <div class="handle-box">
        <el-row>
          <el-col :span="16">
            <!-- 搜索框 -->
            <el-input
              v-model="query.id"
              maxlength="11"
              placeholder="编号"
              class="grid-content handle-input mr10"
              @keyup.enter.native="handleSearch"
            />

            <!-- 其他条件 -->
            <slot name="filter" />

            <!-- 搜索按钮 -->
            <el-button type="primary" :icon="Search" :disabled="!/(^[1-9]\d*$)/.test(query.id)" @click="handleSearch"
              >搜索</el-button
            >

            <!-- 清除按钮 -->
            <el-button type="primary" :icon="Remove" :disabled="query.id.length == 0" @click="handleRemove"
              >清除</el-button
            >
          </el-col>

          <el-col :span="8">
            <!-- 添加按钮 -->
            <el-button type="primary" :icon="Plus" class="grid-content float-right" @click="handleAdd">添 加</el-button>

            <!-- 删除按钮 -->
            <el-button
              type="danger"
              :icon="Delete"
              class="grid-content float-right mr10"
              :disabled="state.selectedList.length == 0"
              @click="handleSelectedDelete"
              >删 除</el-button
            >
          </el-col>
        </el-row>
      </div>

      <!-- 表格数据 -->
      <el-table
        :data="state.isShowSearched ? state.searched : data"
        border
        stripe
        class="table"
        :default-sort="{ prop: 'id', order: 'ascending' }"
        @selection-change="handleSelectionChange"
      >
        <!-- 勾选框 -->
        <el-table-column type="selection" width="80" align="center" />

        <!-- 序号 -->
        <el-table-column
          label="序号"
          type="index"
          width="80"
          align="center"
          fixed
          :index="
            (index: number) => {
              return index + 1 + (query.currentPage - 1) * query.pageSize;
            }
          "
        />

        <!-- 列表数据 -->
        <slot name="tableColumn" />

        <!-- 创建时间和更新时间 -->
        <el-table-column prop="gmt_create" label="创建时间" width="180" align="center" />
        <el-table-column prop="gmt_modify" label="更新时间" width="180" align="center" />

        <!-- 操作 -->
        <el-table-column label="操作" min-width="180" align="center" fixed="right">
          <template #default="scope">
            <el-button type="text" :icon="Edit" @click="handleEdit(scope.row)">编辑</el-button>
            <el-button type="text" :icon="Delete" class="red" @click="handleDelete(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- 分页 -->
      <pagination
        :current-page="query.currentPage"
        :page-size="query.pageSize"
        :page-total="pageTotal"
        :disabled="!state.isShowSearched"
        @page-index="pageIndex"
      />
    </div>

    <!-- 弹出框 -->
    <el-dialog
      :title="`${state.addOrUpdate ? '添加信息' : '编辑信息'}`"
      v-model="state.showDialog"
      width="22%"
      draggable
    >
      <el-form label-width="100px" ref="formRef" :model="props.formData" :rules="props.formRules">
        <slot name="showDialog" />
      </el-form>

      <template #footer>
        <span class="dialog-footer">
          <el-button @click="state.showDialog = false">取 消</el-button>
          <el-button type="primary" v-if="state.addOrUpdate" @click="saveAdd(formRef)">添 加</el-button>
          <el-button type="primary" v-else @click="saveEdit(formRef)">更 新</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<style scoped>
.table {
  width: 100%;
}

.red {
  color: #ff0000;
}

.table-td-thumb {
  display: block;
  margin: auto;
  width: 40px;
  height: 40px;
}

.handle-box {
  margin-bottom: 20px;
}

.handle-input {
  width: 180px;
  display: inline-block;
}

.mr10 {
  margin-right: 10px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.float-right {
  float: right;
}
</style>
