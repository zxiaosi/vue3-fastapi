<script setup lang="ts">
import { reactive, onMounted, inject, onUnmounted } from "vue";
import { UserFilled, List, Promotion } from "@element-plus/icons-vue";
import { getDashboard, getLangList, addTodo, updateTodo } from "@/api/index";
import { getLocal } from "@/request/auth";
import { dateFunction } from "@/utils/handleTime";
import { type State, type Language, RolesEnum } from ".";
import type { UserInfo } from "@/types";

// echarts图
let echarts: any = inject("echarts");

// 缓存的用户信息
const userInfo: UserInfo = reactive(JSON.parse(getLocal("userInfo")));

const state: State = reactive({
  identity: RolesEnum[getLocal("role")], // 角色权限
  langDetails: [], // 语言使用详情
  todoList: [], // 待办列表
  visitNum: 0, // 访问量
  todoNum: 0, // 待办数
  requestNum: 0, // 请求次数
  showDialog: false, // 待办添加弹框
  todoText: "", // 待办文本
});

let pieChart: any;
let barChart: any;

onMounted(async () => {
  await getData();

  pieChart = echarts.init(document.getElementById("pie"));
  barChart = echarts.init(document.getElementById("bar"));
  echartPie();
  eachartBar();
});

// 销毁echarts
onUnmounted(() => {
  pieChart?.dispose();
  barChart?.dispose();
});

/**
 * 获取 语言详情 && 待办事项 || 获取 访问量 && 待办数 && 请求数
 */
const getData = async () => {
  const [{ data: langList }, { data: dashboard }] = await Promise.all([getLangList(), getDashboard()]);
  let item = processData(langList);
  state.langDetails = item;
  state.visitNum = dashboard.visit_num;
  state.todoNum = dashboard.todo_num;
  state.requestNum = dashboard.request_num;
  state.todoList = dashboard.todo_list;
};

/**
 * 随机生成十六进制颜色
 * https://www.jb51.net/article/102109.htm
 */
const randomHexColor = () => {
  return "#" + ("00000" + ((Math.random() * 0x1000000) << 0).toString(16)).slice(-6);
};

/**
 * 加工数据
 * @param data
 */
const processData = (data: any) => {
  let keyList = Object.keys(data); // key列表
  let valueList = Object.values(data); // value列表
  let total = eval(valueList.join("+")); // 总数
  let proportion: number = 0; // 比例
  let item: Language[] = []; // 加工后数据
  for (let i = 0; i < 3; i++) {
    let percentage = Math.trunc((data[keyList[i]] / total) * 100);
    item.push({ title: keyList[i], percentage, color: randomHexColor() });
    proportion += percentage;
  }
  // Other
  item.push({ title: "Other", percentage: 100 - proportion, color: randomHexColor() });
  return item;
};

/**
 * 添加待办事项
 */
const createTodo = async () => {
  const { data } = await addTodo({ title: state.todoText });
  state.todoList = data;
  state.showDialog = false;
  await getData();
  state.todoText = "";
};

/**
 * 勾选待办事项
 */
const modifyTodo = async (index: number) => {
  await updateTodo({ id: index });
  await getData();
};

/**
 * 取消添加事项
 */
const cancel = () => {
  state.showDialog = false;
  state.todoText = "";
};

/**
 * echarts-pie(饼状图)
 */
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
          { value: state.visitNum, name: "用户访问量" },
          { value: state.todoNum, name: "待办事项" },
          { value: state.requestNum, name: "请求次数" },
        ],
      },
    ],
  });
  // 自适应
  window.onresize = function () {
    pieChart.resize();
  };
};

/**
 * echarts-bar(柱状图)
 */
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
            <img :src="userInfo.image" class="user-avator" />
            <div class="user-info-cont">
              <div class="user-info-name">{{ userInfo.name }}</div>
              <div>
                <el-icon size="16" class="el-icon-ali-id" />
                {{ state.identity }}
              </div>
            </div>
          </div>
          <div class="user-info-list">最后更新时间：{{ dateFunction(userInfo.update_time) }}</div>
          <div class="user-info-list">当前登录地址：{{ userInfo.address }}</div>
        </el-card>

        <!-- 语言详情 -->
        <el-card style="height: 250px">
          <template #header>
            <div class="clearfix">
              <span>语言使用详情</span>
            </div>
          </template>

          <!-- 进度条 -->
          <el-table :show-header="false" :data="state.langDetails" class="language">
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
                  <div class="grid-num">{{ state.visitNum }}</div>
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
                  <div class="grid-num">{{ state.todoNum }}</div>
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
                  <div class="grid-num">{{ state.requestNum }}</div>
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
              <el-button size="small" style="float: right" type="primary" @click="state.showDialog = true">添加</el-button>
            </div>
          </template>

          <el-table :show-header="false" :data="state.todoList" style="width: 100%">
            <el-table-column width="40">
              <template #default="scope">
                <el-checkbox v-model="scope.row.status" @change="modifyTodo(scope.$index)" />
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
          <el-button type="primary" @click="createTodo">添 加</el-button>
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

.el-icon-ali-id {
  font-size: 16px;
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

.clearfix {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.todo-item {
  font-size: 14px;
}

.todo-item-del {
  text-decoration: line-through;
  color: #999;
}
</style>
