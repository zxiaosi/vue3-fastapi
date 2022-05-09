<script setup lang="ts">
import { reactive, onMounted, watch } from "vue";
import { useStore } from "@/stores";
import { useRouter } from "vue-router";
import { ElMessage } from "element-plus";
import { Fold, Expand, Bell, CaretBottom } from "@element-plus/icons-vue";
import { getLocal } from "@/request/auth";
import { logout } from "@/api";
import type { UserInfo } from "@/types";

const store = useStore(); // 状态管理
const router = useRouter(); // 全局路由

const userInfo: UserInfo = reactive(JSON.parse(getLocal("userInfo")));

const state = reactive({
  message: 4 as number, // 未读消息
});

onMounted(async () => {
  // 当屏幕宽度小于1500,折叠侧边栏
  if (document.body.clientWidth < 1500) {
    collapseChage();
  }
});

watch(store, (newVal, oldVal) => {
  state.message = newVal.messages;
});

// 侧边栏折叠
const collapseChage = () => {
  store.$patch({ collapse: !store.collapse });
};

/**
 * 用户名下拉菜单选择事件
 * @param command  logout
 */
const handleCommand = async (command: "logout") => {
  if (command == "logout") {
    await logout();
    ElMessage.success("退出登录！");
    router.push("/login");
    localStorage.clear(); // 清除缓存
    store.clearTags(); // 清除标签
  }
};
</script>

<template>
  <div class="header">
    <!-- 折叠按钮 -->
    <div class="collapse-btn" @click="collapseChage">
      <el-icon v-if="!store.collapse"><fold /></el-icon>
      <el-icon v-else><expand /></el-icon>
    </div>

    <!-- logo名 -->
    <div class="logo">学生选课系统</div>

    <!-- 右侧 -->
    <div class="header-right">
      <div class="header-user-con">
        <!-- 消息中心 -->
        <div class="btn-bell">
          <el-badge :is-dot="state.message ? true : false">
            <el-tooltip effect="dark" :content="state.message ? `有${state.message}条未读消息` : `消息中心`" placement="bottom">
              <router-link to="/messages">
                <el-icon :size="22" color="#409EFC"><bell /></el-icon>
              </router-link>
            </el-tooltip>
          </el-badge>
        </div>

        <!-- 用户头像 -->
        <div class="user-avator">
          <img :src="userInfo.image" />
        </div>

        <!-- 用户名下拉菜单 -->
        <el-dropdown trigger="click" @command="handleCommand">
          <span class="el-dropdown-link">
            <span>{{ userInfo.name }}</span>
            <el-icon :size="20"><caret-bottom /></el-icon>
          </span>

          <template #dropdown>
            <el-dropdown-menu>
              <a href="https://github.com/zxiaosi/Vue3-FastAPI" target="_blank">
                <el-dropdown-item>项目仓库</el-dropdown-item>
              </a>
              <el-dropdown-item divided command="logout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
    </div>
  </div>
</template>

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
.user-avator {
  margin: 15px;
}
.user-avator img {
  display: block;
  width: 30px;
  height: 30px;
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
