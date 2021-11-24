<template>
  <div class="header">
    <!-- 折叠按钮 -->
    <div class="collapse-btn" @click="collapseChage">
      <el-icon v-if="!collapse" :size=size>
        <fold />
      </el-icon>
      <el-icon v-else :size=size>
        <expand />
      </el-icon>
    </div>

    <!-- logo名 -->
    <div class="logo">学生选课系统</div>

    <!-- 头部右侧 -->
    <div class="header-right">
      <div class="header-user-con">
        <!-- 消息中心 -->
        <div class="btn-bell">
          <el-tooltip effect="dark" :content="message?`有${message}条未读消息`:`消息中心`" placement="bottom">
            <router-link to="/tabs">
              <el-icon :size=size color="#409EFC">
                <bell />
              </el-icon>
            </router-link>
          </el-tooltip>
          <span class="btn-bell-badge" v-if="message"></span>
        </div>

        <!-- 用户头像 -->
        <div class="user-avator">
          <img src="../assets/img/img.jpg" />
        </div>

        <!-- 用户名下拉菜单 -->
        <el-dropdown class="user-name" trigger="click" @command="handleCommand">
          <span class="el-dropdown-link">
            {{username}}
            <el-icon :size=size>
              <caret-bottom />
            </el-icon>
          </span>
          <template #dropdown>
            <el-dropdown-menu>
              <a href="https://github.com/zxiaosi/Vue3-FastAPI" target="_blank">
                <el-dropdown-item>项目仓库</el-dropdown-item>
              </a>
              <el-dropdown-item command="user">个人中心</el-dropdown-item>
              <el-dropdown-item divided command="loginout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { Expand, Fold, Bell, CaretBottom } from '@element-plus/icons'; // 图标

const username = localStorage.getItem('ms_username');
const message = 2;

const store = useStore();
const size = computed(() => store.state.size); // 设置 element-icon 图标大小
const collapse = computed(() => store.state.collapse); // 设置侧边栏是否折叠

// 侧边栏折叠
const collapseChage = () => {
  store.commit('handleCollapse', !collapse.value);
};

// 当屏幕宽度超多1500,折叠侧边栏
onMounted(() => {
  if (document.body.clientWidth < 1500) {
    collapseChage();
  }
});

// 用户名下拉菜单选择事件
const router = useRouter();
const handleCommand = (command) => {
  if (command == 'loginout') {
    localStorage.removeItem('ms_username');
    router.push('/login');
  } else if (command == 'user') {
    router.push('/user');
  }
};

// defineExpose 可以省略
defineExpose({
  username,
  message,
  size,
  handleCommand,
});
</script>

<style scoped>
.header {
  position: relative;
  box-sizing: border-box;
  width: 100%;
  height: 70px;
  font-size: 22px;
  color: #fff;
}
.collapse-btn {
  float: left;
  padding: 0 21px;
  cursor: pointer;
  line-height: 74px;
}
.header .logo {
  float: left;
  width: 250px;
  line-height: 70px;
}
.header-right {
  float: right;
  padding-right: 50px;
}
.header-user-con {
  display: flex;
  height: 70px;
  align-items: center;
}
.btn-fullscreen {
  transform: rotate(45deg);
  margin-right: 5px;
  font-size: 24px;
}
.btn-bell,
.btn-fullscreen {
  position: relative;
  width: 30px;
  height: 30px;
  text-align: center;
  border-radius: 15px;
  cursor: pointer;
  margin-top: 10px;
}
.btn-bell-badge {
  position: absolute;
  right: 0;
  top: -2px;
  width: 8px;
  height: 8px;
  border-radius: 4px;
  background: #f56c6c;
  color: #fff;
}
.btn-bell .el-icon-bell {
  color: #fff;
}
.user-name {
  margin-left: 10px;
}
.user-avator {
  margin: 0px 20px;
}
.user-avator img {
  display: block;
  width: 40px;
  height: 40px;
  border-radius: 50%;
}
.el-dropdown-link {
  color: #fff;
  cursor: pointer;
  display: flex;
  align-items: center;
}

.el-dropdown-link .el-icon {
  margin-left: 4px;
}

.el-dropdown-menu__item {
  text-align: center;
}
</style>
