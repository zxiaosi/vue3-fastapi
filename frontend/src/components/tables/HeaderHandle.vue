<template>
  <!-- 搜索 -->
  <div class="handle-box">
    <el-row>
      <el-col :span="16">
        <!-- 搜索框 -->
        <el-input v-model="query.id" maxlength="11" placeholder="编号"
          class="grid-content handle-input mr10" />

        <!-- 其他条件 -->
        <slot name="filter" />

        <!-- 搜索按钮 -->
        <el-button type="primary" :icon="Search" :disabled="!/(^[1-9]\d*$)/.test(query.id)"
          @click="handleSearch">搜索</el-button>

        <!-- 清除按钮 -->
        <el-button type="primary" :icon="Remove" :disabled='query.id == 0' @click="handleRemove">清除
        </el-button>
      </el-col>

      <el-col :span="8">
        <!-- 添加按钮 -->
        <el-button type="primary" :icon="Plus" class="grid-content float-right" @click="handleAdd">
          添 加</el-button>

        <!-- 删除按钮 -->
        <el-button type="danger" :icon="Delete" class="grid-content float-right mr10"
          :disabled="selectedList.length == 0" @click="handleSelectedDelete">
          删 除</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { defineProps, defineEmits, toRefs } from '@vue/runtime-core';
import { ElMessage, ElMessageBox } from 'element-plus';
import { Search, Remove, Plus, Delete } from '@element-plus/icons';
import clickRecover from '../../utils/clickRecover';

const props = defineProps({
  query: Object,
  data: Object,
  formData: Object,
  isShowSearched: Boolean,
  selectedList: Array,
  read_datas: Function,
  delete_data: Function,
  removeSearch: Function,
});

const { query, data, formData, isShowSearched, selectedList } = toRefs(props);

const emit = defineEmits(['searchedData', 'isAddDialog']);

// 搜索数据
const handleSearch = (event) => {
  clickRecover(event);
  let isFlag = false;

  data.value.map((item) => {
    if (query.value.id === item.id) {
      isFlag = true;
      props
        .read_datas(query.value.id)
        .then((res) => {
          console.log(res.data)
          emit('searchedData', res.data);
        })
        .catch(() => {
          ElMessage.error('搜索数据失败!');
        });
    }
  });

  if (isFlag === false) {
    ElMessage.warning('编号不存在');
  }
};

// 移除搜索
const handleRemove = (event) => {
  clickRecover(event);

  props.removeSearch();
};

// 删除被勾选的数据
function handleSelectedDelete(event) {
  clickRecover(event);

  // 二次确认删除
  ElMessageBox.confirm('确定要删除吗？', '提示', {
    confirmButtonText: '删除',
    cancelButtonText: '取消',
    type: 'warning',
  })
    .then(() => {
      selectedList.value.map((item) => {
        // 调用删除院系接口
        props
          .delete_data(item.idx)
          .then((res) => {
            if (res.code === 200) {
              data.value.splice(item.reindex, 1);
              props.removeSearch();
              ElMessage.success(`删除编号为${item.idx}的数据成功！`);
            } else {
              ElMessage.warning(`删除编号为${item.idx}的数据失败！`);
            }
          })
          .catch(() => {
            ElMessage.error('删除数据失败！');
          });
      });
    })
    .catch(() => {});
}

// 添加数据按钮
const handleAdd = (event) => {
  clickRecover(event);

  // 重置表单
  Object.keys(formData.value).forEach((key) => (formData.value[key] = ''));

  // 显示添加弹窗
  // showDialog=true addOrUpdate=true
  emit('isAddDialog', true, true);
};

// 可以省略
defineExpose({
  query,
  data,
  formData,
  isShowSearched,
  selectedList,
  handleSearch,
  handleRemove,
  handleSelectedDelete,
  handleAdd,
});
</script>

<style>
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