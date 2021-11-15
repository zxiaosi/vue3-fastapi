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
            当前登录时间：<span>{{currentTime}}</span>
          </div>
          <div class="user-info-list">
            当前登录地点：<span>测试地点</span>
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
              <template #default="scope">
                {{scope.row.title}}
              </template>
            </el-table-column>
            <el-table-column style="width: calc(100% - 140px);">
              <template #default="scope">
                <el-progress :percentage=scope.row.percentage :color=scope.row.color></el-progress>
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
                <i class="el-icon-user-solid grid-con-icon"></i>
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
                <i class="el-icon-message-solid grid-con-icon"></i>
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
                <i class="el-icon-s-goods grid-con-icon"></i>
                <div class="grid-cont-right">
                  <div class="grid-num">5000</div>
                  <div>数量</div>
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
              <el-button style="float: right; padding: 3px 0" type="text"
                @click="showDialog = true">添加</el-button>
            </div>
          </template>

          <el-table :show-header="false" :data="todoList" style="width:100%;">
            <el-table-column width="40">
              <template #default="scope">
                <el-checkbox v-model="scope.row.status"></el-checkbox>
              </template>
            </el-table-column>
            <el-table-column>
              <template #default="scope">
                <div class="todo-item" :class="{'todo-item-del': scope.row.status,}">
                  {{ scope.row.title }}</div>
              </template>
            </el-table-column>
            <el-table-column width="60">
              <template>
                <i class="el-icon-edit"></i>
                <i class="el-icon-delete"></i>
              </template>
            </el-table-column>
          </el-table>
        </el-card>

      </el-col>
    </el-row>

    <!-- 待办事项弹窗 -->
    <el-dialog title="添加待办" v-model="showDialog" width="30%">
      <el-form label-width="100px" autocomplete="on">
        <el-form-item label="待办事项">
          <el-input v-model="text" placeholder="请输入待办事项"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="cancel">取 消</el-button>
          <el-button type="primary" @click="add">添 加</el-button>
        </span>
      </template>
    </el-dialog>

    <!-- schart图表 -->
    <el-row :gutter="20">
      <el-col :span="12">
        <el-card shadow="hover">
          <schart ref="line" class="schart" canvasId="line" :options="options"></schart>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card shadow="hover">
          <schart ref="ring" class="schart" canvasId="ring" :options="options2"></schart>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Schart from 'vue-schart';
import { ref, reactive, onMounted } from 'vue';
export default {
  name: 'dashboard',
  components: { Schart },
  setup() {
    const name = localStorage.getItem('ms_username');
    const role = name === 'admin' ? '超级管理员' : '普通用户';
    const currentTime = ref(0);

    // 当前登录时间
    onMounted(() => {
      var aData = new Date();
      currentTime.value =
        aData.getFullYear() +
        '年' +
        (aData.getMonth() + 1) +
        '月' +
        aData.getDate() +
        '日';
    });

    // 语言使用详情
    const languages = reactive([
      { title: 'Vue', percentage: 53.4, color: '#42b983' },
      { title: 'Python', percentage: 38.2, color: '#f1e05a' },
      { title: 'JavaScript', percentage: 6.3, color: '#409EFF' },
      { title: 'CSS', percentage: 1.7, color: '#f56c6c' },
    ]);

    // 待办
    const showDialog = ref(false);
    const todoList = reactive([
      { title: '调整代码结构', status: false },
      { title: '添加学生表信息', status: false },
      { title: '添加教师表信息', status: false },
      { title: '添加专业表信息', status: true },
      { title: '修改首页内容', status: true },
      { title: '添加了院系表(见信息表格)', status: true },
    ]);

    // 折线图
    const options = {
      type: 'line',
      title: { text: '最近一周的代码提交' },
      labels: ['周一', '周二', '周三', '周四', '周五'],
      datasets: [
        { label: 'GitLab', data: [23, 27, 27, 19, 23] },
        { label: 'Github', data: [16, 17, 19, 13, 16] },
        { label: 'Gitee', data: [18, 19, 15, 23, 12] },
      ],
    };

    // 环状图
    const options2 = {
      type: 'ring',
      title: { text: '最近一周工作状态' },
      legend: { position: 'left' },
      labels: ['上班', '前端', '后端', 'Bug'],
      datasets: [{ data: [50, 20, 20, 30] }],
    };

    // 添加待办
    const text = ref('');
    const add = () => {
      todoList.pop();
      todoList.unshift({ title: text.value, status: false });
      showDialog.value = false;
      text.value = '';
    };

    // 取消
    const cancel = () => {
      showDialog.value = false;
      text.value = '';
    };

    return {
      name,
      currentTime,
      languages,
      options,
      options2,
      showDialog,
      todoList,
      role,
      text,
      add,
      cancel,
    };
  },
};
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
  line-height: 100px;
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

.schart {
  width: 100%;
  height: 300px;
}
</style>
