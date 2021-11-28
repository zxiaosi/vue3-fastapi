<template>
  <!-- 搜索 -->
  <div class="handle-box">
    <el-select v-model="query.sort" placeholder="排序" class="handle-select mr10">
      <el-option key="1" label="升序" value="up" />
      <el-option key="2" label="降序" value="down" />
    </el-select>
    <el-button type="primary" :icon="Sort" @click="handleSort">排序</el-button>
    <el-button type="primary" :icon="Plus" @click="handleAdd">添加</el-button>
  </div>
</template>

<script setup>
import { toRefs } from 'vue';
import { defineProps, defineEmits } from '@vue/runtime-core';
import { Sort, Plus } from '@element-plus/icons';

const props = defineProps({
  query: Object,
  data: Object,
  formData: Object,
});

const { query, data, formData } = toRefs(props);

const emit = defineEmits(['isAddDialog']);

/**
 * handleSort
 * 升序操作
 */
const handleSort = (event) => {
  clickRecover(event);

  if (query.value.sort === 'up') {
    data.value.sort((a, b) => a.id - b.id);
  } else {
    data.value.sort((a, b) => b.id - a.id);
  }
};

// 添加用户信息
const handleAdd = (event) => {
  clickRecover(event);

  // 重置表单
  Object.keys(formData).forEach((key) => (formData[key] = ''));

  // 显示添加弹窗
  // showDialog=true addOrUpdate=true
  emit('isAddDialog', true);
};

/**
 * clickRecover
 * 点击后鼠标移开恢复按钮默认样式
 */
const clickRecover = (event) => {
  let target = event.target;
  // (如果按钮没有加icon图标的话，target.nodeName == "I"可以去掉)
  if (target.nodeName == 'I' || target.nodeName == 'SPAN') {
    target = event.target.parentNode;
  }
  target.blur();
};

// 可以省略
defineExpose({
  handleSort,
  handleAdd,
});
</script>

<style>
.handle-box {
  margin-bottom: 20px;
}

.handle-select {
  width: 120px;
}

.mr10 {
  margin-right: 10px;
}
</style>