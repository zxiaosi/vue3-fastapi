<script setup lang="ts">
import { reactive, onMounted, inject, onUnmounted, watchEffect } from "vue";
import { useStore } from "@/stores";
import { UserFilled, List, Promotion } from "@element-plus/icons-vue";
import { get_lang_todo_list, get_visit_todo_request, add_todo, update_todo } from "@/api/index";
import { getLocal, setLocal } from "@/request/auth";
import { dateFunction } from "@/utils/handleTime";
import type { stateType } from ".";

// echarts图
let echarts: any = inject("echarts");

// 状态管理
const store = useStore();

const state: stateType = reactive({
  userInfo: JSON.parse(getLocal("userInfo")), // 缓存的用户信息
  languageDetails: [], // 语言使用详情
  todoList: [], // 待办列表
  visitNumber: 0, // 访问量
  todoNumber: 0, // 待办数
  requestNumber: 0, // 请求次数
  showDialog: false, // 待办添加弹框
  todoText: "", // 待办文本
});

watchEffect(() => {
  let user = JSON.parse(getLocal("userInfo"));
  if (store.userInfo.avatar) {
    state.userInfo = store.userInfo;
  } else {
    state.userInfo = user;
  }
});

let pieChart: any;
let barChart: any;

onMounted(async () => {
  pieChart = echarts.init(document.getElementById("pie"));
  barChart = echarts.init(document.getElementById("bar"));

  await getVisitTodoRequest();
  await getLangTodoList();

  echartPie();
  eachartBar();
});

// 销毁echarts
onUnmounted(() => {
  pieChart.dispose();
  barChart.dispose();
});

/**
 * 获取 语言详情 && 待办事项
 */
const getLangTodoList = async () => {
  const { data } = await get_lang_todo_list();
  state.todoList = data.todo_list;
  state.languageDetails = data.language_details;
};

/**
 * 获取 访问量 && 待办数 && 请求数
 */
const getVisitTodoRequest = async () => {
  const { data } = await get_visit_todo_request();
  state.visitNumber = data.visit_num;
  state.todoNumber = data.todo_num;
  state.requestNumber = data.request_num;
};

// 添加待办
const addTodo = async () => {
  const { data } = await add_todo({ title: state.todoText });
  state.todoList = data;
  state.showDialog = false;
  await getVisitTodoRequest();
  state.todoText = "";
};

// 勾选待办
const updateTodo = async (index: number) => {
  await update_todo({ id: index });
};

// 取消
const cancel = () => {
  state.showDialog = false;
  state.todoText = "";
};

// echarts-pie
const echartPie = () => {
  pieChart.setOption({
    title: { text: "信息", left: "center", top: "center" },
    legend: { orient: "vertical", left: "left", data: ["用户访问量", "待办事项", "请求次数"] },
    tooltip: { trigger: "item", formatter: "{b} : {c} ({d}%)" },
    series: [
      {
        type: "pie",
        radius: ["40%", "70%"],
        data: [
          { value: state.visitNumber, name: "用户访问量" },
          { value: state.todoNumber, name: "待办事项" },
          { value: state.requestNumber, name: "请求次数" },
        ],
      },
    ],
  });
  // 自适应
  window.onresize = function () {
    pieChart.resize();
  };
};

// echarts-bar
const eachartBar = () => {
  barChart.setOption({
    title: { text: "周进度", left: "center" },
    legend: { show: true },
    tooltip: { trigger: "item", formatter: "{b} : {c}" },
    xAxis: { data: ["周一", "周二", "周三", "周四", "周五", "周六", "周日"] },
    yAxis: {},
    series: [{ type: "bar", data: [23, 24, 18, 25, 27, 28, 25] }],
  });
  // 自适应
  window.onresize = function () {
    barChart.resize();
  };
};
</script>

<template>
  <div class="body">
    <!-- 用户信息、访问量、语言详情、待办事项 -->
    <el-row :gutter="20">
      <el-col :span="8">
        <!-- 用户信息 -->
        <el-card class="mgb20" style="height: 252px">
          <div class="user-info">
            <img :src="state.userInfo.avatar" class="user-avator" />
            <div class="user-info-cont">
              <div class="user-info-name">{{ state.userInfo.name }}</div>
              <div>{{ state.userInfo.name === "admin" ? "超级管理员" : "普通用户" }}</div>
            </div>
          </div>
          <div class="user-info-list">最后更新时间：{{ dateFunction(state.userInfo.modifyTime) }}</div>
          <div class="user-info-list">当前登录地址：{{ state.userInfo.address }}</div>
        </el-card>

        <!-- 语言详情 -->
        <el-card style="height: 250px">
          <template #header>
            <div class="clearfix">
              <span>语言使用详情</span>
            </div>
          </template>

          <!-- 进度条 -->
          <el-table :show-header="false" :data="state.languageDetails" class="language">
            <el-table-column width="100">
              <template #default="scope">{{ scope.row.title }}</template>
            </el-table-column>

            <el-table-column style="width: calc(100% - 140px)">
              <template #default="scope">
                <el-progress :percentage="scope.row.percentage" :color="scope.row.color" />
              </template>
            </el-table-column>
          </el-table>
        </el-card>
      </el-col>

      <!-- 访问量、消息、数量、待办 -->
      <el-col :span="16">
        <!-- 访问量、消息、数量 -->
        <el-row :gutter="20" class="mgb20">
          <el-col :span="8">
            <el-card :body-style="{ padding: '0px' }">
              <div class="grid-content grid-con-1">
                <el-icon class="grid-con-icon"><user-filled /></el-icon>
                <div class="grid-cont-right">
                  <div class="grid-num">{{ state.visitNumber }}</div>
                  <div>用户访问量</div>
                </div>
              </div>
            </el-card>
          </el-col>

          <el-col :span="8">
            <el-card :body-style="{ padding: '0px' }">
              <div class="grid-content grid-con-2">
                <el-icon class="grid-con-icon"><list /></el-icon>
                <div class="grid-cont-right">
                  <div class="grid-num">{{ state.todoNumber }}</div>
                  <div>待办事项</div>
                </div>
              </div>
            </el-card>
          </el-col>

          <el-col :span="8">
            <el-card :body-style="{ padding: '0px' }">
              <div class="grid-content grid-con-3">
                <el-icon class="grid-con-icon"><promotion /></el-icon>
                <div class="grid-cont-right">
                  <div class="grid-num">{{ state.requestNumber }}</div>
                  <div>请求次数</div>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>

        <!-- 待办 -->
        <el-card style="height: 402px">
          <template #header>
            <div class="clearfix">
              <span>待办事项</span>
              <el-button style="float: right; padding: 3px 0" type="text" @click="state.showDialog = true"
                >添加</el-button
              >
            </div>
          </template>

          <el-table :show-header="false" :data="state.todoList" style="width: 100%">
            <el-table-column width="40">
              <template #default="scope">
                <el-checkbox v-model="scope.row.status" @change="updateTodo(scope.$index)" />
              </template>
            </el-table-column>

            <!-- 待办内容 -->
            <el-table-column>
              <template #default="scope">
                <div class="todo-item" :class="{ 'todo-item-del': scope.row.status }">
                  {{ scope.row.title }}
                </div>
              </template>
            </el-table-column>
          </el-table>
        </el-card>
      </el-col>
    </el-row>

    <!-- echarts图 -->
    <el-row :gutter="20" style="margin-bottom: -10px">
      <el-col :span="8">
        <el-card>
          <div id="pie" style="height: 220px" />
        </el-card>
      </el-col>

      <el-col :span="16">
        <el-card>
          <div id="bar" style="height: 220px" />
        </el-card>
      </el-col>
    </el-row>

    <!-- 待办事项弹窗 -->
    <el-dialog title="添加待办" v-model="state.showDialog" width="21%" draggable>
      <el-form label-width="100px" autocomplete="on">
        <el-form-item label="待办事项">
          <el-input v-model="state.todoText" placeholder="请输入待办事项" />
        </el-form-item>
      </el-form>

      <template #footer>
        <span class="dialog-footer">
          <el-button @click="cancel">取 消</el-button>
          <el-button type="primary" @click="addTodo">添 加</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<style scoped>
/* 屏幕最小宽度 */
.body {
  min-width: 1500px;
}

.el-row {
  margin-bottom: 20px;
}

.grid-content {
  display: flex;
  align-items: center;
  height: 100px;
}

.grid-cont-right {
  flex: 1;
  text-align: center;
  font-size: 14px;
  color: #999;
}

.grid-num {
  font-size: 30px;
  font-weight: bold;
}

.grid-con-icon {
  font-size: 50px;
  width: 100px;
  height: 100px;
  text-align: center;
  line-height: 112px;
  color: #fff;
}

.grid-con-1 .grid-con-icon {
  background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
  color: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
  background: rgb(100, 213, 114);
}

.grid-con-2 .grid-num {
  color: rgb(45, 140, 240);
}

.grid-con-3 .grid-con-icon {
  background: rgb(242, 94, 67);
}

.grid-con-3 .grid-num {
  color: rgb(242, 94, 67);
}

.user-info {
  display: flex;
  align-items: center;
  padding-bottom: 20px;
  border-bottom: 2px solid #ccc;
  margin-bottom: 20px;
}

.user-avator {
  width: 120px;
  height: 120px;
  border-radius: 50%;
}

.user-info-cont {
  padding-left: 50px;
  flex: 1;
  font-size: 14px;
  color: #999;
}

.user-info-cont div:first-child {
  font-size: 30px;
  color: #222;
}

.user-info-list {
  font-size: 14px;
  color: #999;
  line-height: 25px;
}

.user-info-list span {
  margin-left: 70px;
}

/* 语言使用详情 */
.language {
  width: 100%;
  margin-top: -8px;
}

.mgb20 {
  margin-bottom: 20px;
}

.todo-item {
  font-size: 14px;
}

.todo-item-del {
  text-decoration: line-through;
  color: #999;
}
</style>
