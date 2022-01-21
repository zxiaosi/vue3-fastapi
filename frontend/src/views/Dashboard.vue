<template>
  <div>
    <!-- 用户信息、访问量、语言详情、待办事项 -->
    <el-row :gutter="20">
      <el-col :span="8">
        <!-- 用户信息 -->
        <el-card shadow="hover" class="mgb20" style="height:252px;">
          <div class="user-info">
            <img src="../assets/img/img.jpg" class="user-avator" alt />
            <div class="user-info-cont">
              <div class="user-info-name">{{ name }}</div>
              <div>{{ role }}</div>
            </div>
          </div>
          <div class="user-info-list">
            当前登录时间：
            <span>{{ state.currentTime }}</span>
          </div>
          <div class="user-info-list">
            当前登录地点：
            <span>测试地点</span>
          </div>
        </el-card>

        <!-- 语言详情 -->
        <el-card shadow="hover" style="height:252px;">
          <template #header>
            <div class="clearfix">
              <span>语言使用详情</span>
            </div>
          </template>

          <!-- 进度条 -->
          <el-table :show-header="false" :data="languages" class="language">
            <el-table-column width="100">
              <template #default="scope">{{ scope.row.title }}</template>
            </el-table-column>
            <el-table-column style="width: calc(100% - 140px);">
              <template #default="scope">
                <el-progress :percentage="scope.row.percentage" :color="scope.row.color" />
              </template>
            </el-table-column>
          </el-table>
        </el-card>
      </el-col>

      <el-col :span="16">
        <!-- 访问量、消息、数量 -->
        <el-row :gutter="20" class="mgb20">
          <el-col :span="8">
            <el-card shadow="hover" :body-style="{ padding: '0px' }">
              <div class="grid-content grid-con-1">
                <el-icon class="grid-con-icon">
                  <user-filled />
                </el-icon>
                <div class="grid-cont-right">
                  <div class="grid-num">1234</div>
                  <div>用户访问量</div>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :span="8">
            <el-card shadow="hover" :body-style="{ padding: '0px' }">
              <div class="grid-content grid-con-2">
                <el-icon class="grid-con-icon">
                  <message />
                </el-icon>
                <div class="grid-cont-right">
                  <div class="grid-num">321</div>
                  <div>系统消息</div>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :span="8">
            <el-card shadow="hover" :body-style="{ padding: '0px' }">
              <div class="grid-content grid-con-3">
                <el-icon class="grid-con-icon">
                  <promotion />
                </el-icon>
                <div class="grid-cont-right">
                  <div class="grid-num">{{ state.request_num }}</div>
                  <div>请求次数</div>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>

        <!-- 待办 -->
        <el-card shadow="hover" style="height:403px;">
          <template #header>
            <div class="clearfix">
              <span>待办事项</span>
              <el-button style="float: right; padding: 3px 0" type="text" @click="showDialog = true">添加</el-button>
            </div>
          </template>

          <el-table :show-header="false" :data="state.todoList" style="width:100%;">
            <!-- 选择框 -->
            <el-table-column width="40">
              <template #default="scope">
                <el-checkbox v-model="scope.row.status" @change="update(scope.$index)" />
              </template>
            </el-table-column>

            <!-- 待办内容 -->
            <el-table-column>
              <template #default="scope">
                <div class="todo-item" :class="{ 'todo-item-del': scope.row.status }">{{ scope.row.title }}</div>
              </template>
            </el-table-column>
          </el-table>
        </el-card>
      </el-col>

      <el-row class="githubCard">
        <el-col :span="8">
          <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=zxiaosi&layout=compact" />
        </el-col>

        <el-col :span="10">
          <img
            src="https://github-readme-stats.vercel.app/api?username=zxiaosi&hide=prs&show_icons=true&theme=tokyonight" />
        </el-col>
      </el-row>
    </el-row>

    <!-- 待办事项弹窗 -->
    <el-dialog title="添加待办" v-model="showDialog" width="30%">
      <el-form label-width="100px" autocomplete="on">
        <el-form-item label="待办事项">
          <el-input v-model="state.todoText" placeholder="请输入待办事项"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="cancel">取 消</el-button>
          <el-button type="primary" @click="add">添 加</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import {
  UserFilled,
  Message,
  Goods,
  Edit,
  Delete,
  Promotion,
} from '@element-plus/icons'; // 图标
import { get_dashboard, add_todo, update_todo } from '@api/dashboard';

const name = localStorage.getItem('ms_username');
const role = name === 'admin' ? '超级管理员' : '普通用户';

const state = reactive({
  currentTime: 0, // 当前时间
  request_num: 0, // 请求次数
  todoList: [], // 待办列表
  todoText: '', // 待办文本
});

// 当前登录时间
onMounted(() => {
  var aData = new Date();
  state.currentTime =
    aData.getFullYear() +
    '年' +
    (aData.getMonth() + 1) +
    '月' +
    aData.getDate() +
    '日';

  getData();
});

/**
 * 获取数据
 */
async function getData() {
  let res = await get_dashboard();
  state.request_num = res.data.request_num;
  state.todoList = res.data.todoList;
}

// 语言使用详情
const languages = reactive([
  { title: 'Vue', percentage: 53.4, color: '#42b983' },
  { title: 'Python', percentage: 38.2, color: '#f1e05a' },
  { title: 'JavaScript', percentage: 6.3, color: '#409EFF' },
  { title: 'CSS', percentage: 1.7, color: '#f56c6c' },
]);

// 待办添加弹框
const showDialog = ref(false);

// 添加待办
async function add() {
  let res = await add_todo(state.todoText);
  state.todoList = res.data;
  showDialog.value = false;
  state.todoText = '';
}

// 勾选待办
async function update(res) {
  console.log(res);
  await update_todo(res);
}

// 取消
const cancel = () => {
  showDialog.value = false;
  state.todoText = '';
};

// 默认开启,可不要
defineExpose({
  role,
  languages,
  add,
  cancel,
});
</script>

<style scoped>
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
  margin-top: -19px;
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

.githubCard {
  width: 100%;
  margin: 20px 0px 0px 70px;
  justify-content: space-between;
}
</style>
