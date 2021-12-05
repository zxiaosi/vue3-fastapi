<template>
  <!-- 操作 -->
  <el-table-column label="操作" width="220" align="center" fixed='right'>
    <template #default="scope">
      <el-button type="text" :icon="Edit" @click="handleEdit(scope.$index, scope.row)">
        编辑
      </el-button>
      <el-button type="text" :icon="Delete" class="red"
        @click="handleDelete(scope.$index, scope.row)">删除
      </el-button>
    </template>
  </el-table-column>
</template>

<script setup>
import { defineProps, defineEmits, toRefs } from '@vue/runtime-core';
import { ElMessage, ElMessageBox } from 'element-plus';
import { Edit, Delete } from '@element-plus/icons'; // 图标

const props = defineProps({
  data: Object,
  formData: Object,
  delete_data: Function,
  removeSearch: Function,
});
const { data, formData } = toRefs(props);

const emit = defineEmits(['isAddDialog', 'subIndexId']);

/**
 * 编辑院系信息
 */
function handleEdit(index, row) {
  Object.keys(formData.value).forEach((item) => {
    formData.value[item] = row[item];
  });

  // 显示更新弹窗
  // showDialog=true addOrUpdate=true
  emit('isAddDialog', true, false);
  // index-索引, row.id-编号
  emit('subIndexId', index, row.id);
}

/**
 * 删除操作
 */
function handleDelete(index, row) {
  // 二次确认删除
  ElMessageBox.confirm('确定要删除吗？', '提示', {
    confirmButtonText: '删除',
    cancelButtonText: '取消',
    type: 'warning',
  })
    .then(() => {
      // 调用删除院系接口
      props
        .delete_data(row.id)
        .then((res) => {
          if (res.code === 200) {
            data.value.splice(index, 1);
            props.removeSearch();
            ElMessage.success(`删除编号为${row.id}的数据成功！`);
          } else {
            ElMessage.warning(`删除编号为${row.id}的数据失败！`);
          }
        })
        .catch(() => {
          ElMessage.error('删除数据失败！');
        });
    })
    .catch(() => {});
}

// 可以省略
defineExpose({
  data,
  formData,
  handleEdit,
  handleDelete,
});
</script>

<style scoped>
.red {
  color: #ff0000;
}
</style>

