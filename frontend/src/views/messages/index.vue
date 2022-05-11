<script setup lang="ts">
import { ref, reactive } from "vue";
import { useStore } from "@/stores";
import { ElMessage } from "element-plus";
import type { State } from ".";

const store = useStore(); // 状态管理

const message = ref<string>("first");

const state: State = reactive({
  unread: [
    { date: "2022-05-10 10:00:00", title: "此处是假数据, 刷新页面数据回来了(功能还没做😅)！！！" },
    { date: "2022-05-09 21:00:00", title: "完了芭比Q了, bug修不完了😭😭😭！！！" },
    { date: "2022-05-09 08:00:00", title: "你这个年纪你怎么睡得着的😴！！！" },
    { date: "2022-05-08 20:00:00", title: "【系统通知】该系统将于明天凌晨2点到5点进行升级维护🎉🎉🎉！！！" },
  ],
  read: [
    { date: "2022-05-08 08:00:00", title: "你这个年纪你怎么睡得着的😴！！！" },
    { date: "2022-03-02 08:00:00", title: "勇敢牛牛不怕困难！😼" },
  ],
  recycle: [{ date: "2021-11-09 21:00:00", title: "打工人, 打工魂, 打工都是人上人！！！" }],
});

/**
 * 读消息
 */
const handleRead = (index: number) => {
  const item = state.unread.splice(index, 1);
  state.read = item.concat(state.read);
  if (store.messages > 0) {
    store.$patch({ messages: store.messages - 1 });
  } else {
    store.$patch({ messages: 0 });
  }
};

/**
 * 读取全部消息
 */
const readAll = () => {
  state.read = state.unread.concat(state.read);
  state.unread = [];
};

/**
 * 删除全部消息
 */
const deleteAll = () => {
  state.recycle = state.read.concat(state.recycle);
  state.read = [];
};

/**
 * 清空回收站
 */
const emptyRecycle = () => {
  ElMessage.warning("请联系管理员清空回收站！！");
};

/**
 * 删除消息
 */
const handleDel = (index: number) => {
  const item = state.read.splice(index, 1);
  state.recycle = item.concat(state.recycle);
};

/**
 * 还原消息
 */
const handleRestore = (index: number) => {
  const item = state.recycle.splice(index, 1);
  state.read = item.concat(state.read);
};
</script>

<template>
  <div class="">
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item><i class="el-icon-ali-copy" /> tab选项卡</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="container">
      <el-tabs v-model="message">
        <el-tab-pane :label="`未读消息(${state.unread.length})`" name="first">
          <el-table :data="state.unread" :show-header="false" style="width: 100%">
            <el-table-column>
              <template #default="scope">
                <span class="message-title">{{ scope.row.title }}</span>
              </template>
            </el-table-column>

            <el-table-column prop="date" width="180" />

            <el-table-column width="120">
              <template #default="scope">
                <el-button size="small" @click="handleRead(scope.$index)">标为已读</el-button>
              </template>
            </el-table-column>
          </el-table>

          <div class="handle-row">
            <el-button type="primary" @click="readAll()">全部标为已读</el-button>
          </div>
        </el-tab-pane>

        <el-tab-pane :label="`已读消息(${state.read.length})`" name="second">
          <template v-if="message === 'second'">
            <el-table :data="state.read" :show-header="false" style="width: 100%">
              <el-table-column>
                <template #default="scope">
                  <span class="message-title">{{ scope.row.title }}</span>
                </template>
              </el-table-column>
              <el-table-column prop="date" width="150"></el-table-column>
              <el-table-column width="120">
                <template #default="scope">
                  <el-button type="danger" @click="handleDel(scope.$index)">删除</el-button>
                </template>
              </el-table-column>
            </el-table>
            <div class="handle-row">
              <el-button type="danger" @click="deleteAll()">删除全部</el-button>
            </div>
          </template>
        </el-tab-pane>

        <el-tab-pane :label="`回收站(${state.recycle.length})`" name="third">
          <template v-if="message === 'third'">
            <el-table :data="state.recycle" :show-header="false" style="width: 100%">
              <el-table-column>
                <template #default="scope">
                  <span class="message-title">{{ scope.row.title }}</span>
                </template>
              </el-table-column>

              <el-table-column prop="date" width="150" />

              <el-table-column width="120">
                <template #default="scope">
                  <el-button @click="handleRestore(scope.$index)">还原</el-button>
                </template>
              </el-table-column>
            </el-table>

            <div class="handle-row">
              <el-button type="danger" @click="emptyRecycle()">清空回收站</el-button>
            </div>
          </template>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<style>
.message-title {
  cursor: pointer;
}
.handle-row {
  margin-top: 30px;
}
</style>
