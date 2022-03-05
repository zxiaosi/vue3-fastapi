<script setup lang="ts">
import { inject, onMounted, reactive } from "vue";
import { useStore } from "@/stores";
import { useRouter } from "vue-router";
import { ElMessage, ElMessageBox } from "element-plus";
import { Fold, Expand, Bell, CaretBottom, UploadFilled } from "@element-plus/icons-vue";
import { getLocal, removeLocal } from "@/request/auth";
import { get_current_user, logout } from "@/api";
import { API_URL, BASE_URL } from "@/assets/global";

const store = useStore(); // 状态管理
const router = useRouter(); // 全局路由

const username = getLocal("username"); // 本地存储

//获取token，并将其添加至请求头中
let token = getLocal("Authorization");
let header = { Authorization: "Bearer " + token }; // token一定要加 Bearer

const state = reactive({
  api_url: API_URL + "/upload/file/", // 上传图片请求接口
  message: 2, // 未读消息
  dialogVisible: false, // 是否显示弹窗
  image: "", // 头像
});

onMounted(async () => {
  await getUserInfo();
});

const getUserInfo = async () => {
  const { data } = await get_current_user();
  state.image = BASE_URL + data.image;
};

const success = (response: any) => {
  ElMessage.success(response.msg);
  state.dialogVisible = false;
  getUserInfo();
  store.refreshView = true;
};

const error = (err: any) => {
  ElMessage.error(err.msg);
};

onMounted(async () => {
  // 当屏幕宽度小于1500,折叠侧边栏
  if (document.body.clientWidth < 1500) {
    collapseChage();
  }

  await getUserInfo();
});

// 侧边栏折叠
const collapseChage = () => {
  store.$patch({ collapse: !store.collapse });
};

/**
 * 用户名下拉菜单选择事件
 * @param command  logout | upload
 */
const handleCommand = async (command: "logout" | "upload") => {
  if (command == "logout") {
    await logout();
    ElMessage.success("退出登录！");
    removeLocal("username");
    removeLocal("Authorization");
    router.push("/login");
  } else {
    state.dialogVisible = true;
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
            <el-tooltip
              effect="dark"
              :content="state.message ? `有${state.message}条未读消息` : `消息中心`"
              placement="bottom"
            >
              <router-link to="/tabs">
                <el-icon :size="22" color="#409EFC"><bell /></el-icon>
              </router-link>
            </el-tooltip>
          </el-badge>
        </div>

        <!-- 用户头像 -->
        <div class="user-avator">
          <template v-if="state.image">
            <img :src="state.image" />
          </template>
          <template v-else>
            <img src="../assets/img/img.jpg" />
          </template>
        </div>

        <!-- 用户名下拉菜单 -->
        <el-dropdown trigger="click" @command="handleCommand">
          <span class="el-dropdown-link">
            <span>{{ username }}</span>
            <el-icon :size="20"><caret-bottom /></el-icon>
          </span>

          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item command="upload">更换头像</el-dropdown-item>
              <a href="https://github.com/zxiaosi/Vue3-FastAPI" target="_blank">
                <el-dropdown-item>项目仓库</el-dropdown-item>
              </a>
              <el-dropdown-item divided command="logout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
    </div>

    <!-- 头像上传弹窗 -->
    <el-dialog v-model="state.dialogVisible" title="Tips" width="21%">
      <el-upload class="upload" drag :action="state.api_url" :on-success="success" :on-error="error" :headers="header">
        <el-icon class="el-icon--upload"><upload-filled /></el-icon>
        <div class="el-upload__text">Drop file here or <em>click to upload</em></div>
        <template #tip>
          <div class="el-upload__tip">jpg/png文件大小要少于500kb</div>
        </template>
      </el-upload>
    </el-dialog>
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
