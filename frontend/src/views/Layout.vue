<script setup lang="ts">
import { useUserStore } from "@/stores";
import { ICON_URL, IMAGE_URL } from "@/assets/js/global";
import { useRouter } from "vue-router";
import { userLogout } from "@/apis";
import { clearLocal } from "@/request/auth";
import { TITLE } from "@/assets/js/global";
import { pageTo } from "@/utils/handle_data";
import world from "@/assets/img/logo.png";
import { computed } from "vue";

const router = useRouter();
const userStore = useUserStore();
const userInfo = computed(() => userStore.user);

/** 退出登录 */
const handleLogout = async () => {
  await userLogout();
  clearLocal();
  router.push("/login");
  userStore.menu = [];
};
</script>

<template>
  <el-container class="pages">
    <el-aside>
      <div class="logo" @click="pageTo(router, '/')">
        <img :src="world" />
        <span>{{ TITLE }}</span>
      </div>

      <el-menu
        router
        unique-opened
        background-color="#324157"
        text-color="#FFFFFF"
        active-text-color="#409EFF"
        :collapse-transition="false"
        :default-active="router.currentRoute.value.path"
      >
        <template v-for="item in userStore.menu">
          <!-- 二级菜单 -->
          <template v-if="item.children.length > 0">
            <el-sub-menu :index="item.path">
              <template #title>
                <el-image :src="ICON_URL + item.meta.icon" />
                <span>{{ item.meta.title }}</span>
              </template>

              <template v-for="subItem in item.children">
                <el-menu-item :index="subItem.path">
                  <el-image :src="ICON_URL + subItem.meta.icon" />
                  <template #title>{{ subItem.meta.title }}</template>
                </el-menu-item>
              </template>
            </el-sub-menu>
          </template>

          <!-- 一级菜单 -->
          <template v-else>
            <el-menu-item :index="item.path">
              <el-image :src="ICON_URL + item.meta.icon" />
              <template #title>{{ item.meta.title }}</template>
            </el-menu-item>
          </template>
        </template>
      </el-menu>
    </el-aside>

    <el-container>
      <el-header>
        <div class="header-left">
          <el-breadcrumb separator="/">
            <el-breadcrumb-item v-for="item in router.currentRoute.value.matched" :key="item.path">
              <!-- <router-link :to="{ path: item.path }">{{ item.meta.title }}</router-link> -->
              <span>{{ item.meta.title }}</span>
            </el-breadcrumb-item>
          </el-breadcrumb>
        </div>

        <div class="header-right">
          <el-image v-if="userInfo.avatar" :src="IMAGE_URL + userInfo.avatar" />
          <el-image v-else src="https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg" />

          <el-dropdown>
            <span class="el-dropdown-link"> {{ userInfo.name || "未知" }}</span>

            <template #dropdown>
              <el-dropdown-menu>
                <a href="https://gitee.com/zxiaosi/fast-api.git" target="_blank">
                  <el-dropdown-item>项目仓库</el-dropdown-item>
                </a>
                <el-dropdown-item divided @click="handleLogout()">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>

      <el-container class="content">
        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </el-container>
</template>

<style scoped lang="less">
.pages {
  min-width: 1200px;

  .el-aside {
    width: 200px;
    min-width: 200px;
    height: 100vh;
    background-color: #324157;
    color: #ffffff;

    .logo {
      height: 60px;
      line-height: 60px;
      text-align: center;
      font-size: 24px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;

      img {
        width: 24px;
        height: 24px;
        margin-right: 10px;
      }
    }

    .el-menu {
      border-right: none;

      .el-sub-menu,
      .el-menu-item {
        .el-image {
          width: 20px;
          height: 20px;
          background-color: #adb9c9;
          margin-right: 10px;
          display: flex;
          align-items: center;
          justify-content: center;
        }
      }
    }
  }

  .el-header {
    position: relative;
    color: #ffffff;
    background-color: #242f42;
    padding: 10px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;

    .header-left {
      .el-breadcrumb {
        font-size: 16px;
        padding: 10px;

        .router-link-active {
          color: #fff;
          font-weight: 400;
        }
      }

      span {
        color: #fff;
        font-weight: 400;
      }
    }

    .header-right {
      display: flex;
      align-items: center;
      justify-content: center;

      .el-image {
        width: 28px;
        height: 28px;
        border-radius: 50%;
        margin-right: 15px;
      }

      .el-dropdown {
        color: #ffffff;
        font-size: 18px;

        .el-dropdown-link {
          display: flex;
        }

        .el-dropdown-link:focus-visible {
          outline: unset;
        }
      }
    }
  }

  .content {
    padding: 0;
    background-color: #f0f0f0;
    overflow-y: auto;
    max-height: calc(100vh - 60px);

    .el-main {
      height: max-content;
      background: #fff;
      border-radius: 5px;
      border: 1px solid #ddd;
      margin: 20px;
    }
  }
}
</style>
