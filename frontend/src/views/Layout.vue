<script setup lang="ts">
import { useUserStore } from "@/stores";
import { IMAGE_URL } from "@/assets/js/global";
import { useRouter } from "vue-router";
import { computed, onMounted } from "vue";

const router = useRouter();
const userStore = useUserStore();

/** 选中菜单 */
const selectMenu = (menu: any) => {
  router.push(menu.path);
};
</script>

<template>
  <div class="layout-page">
    <el-container>
      <el-header>
        <div class="left">
          <div class="sidebar-btn" @click="userStore.toggleSidebar">
            <el-icon v-if="userStore.isOpenSidebar">
              <Fold />
            </el-icon>
            <el-icon v-else>
              <Expand />
            </el-icon>
          </div>

          <div class="title">Demo</div>
        </div>
        <div class="right"></div>
      </el-header>

      <el-container>
        <!-- 加el-aside为了动画 -->
        <el-aside :width="userStore.isOpenSidebar ? '200px' : '64px'">
          <el-menu
            router
            unique-opened
            background-color="#324157"
            text-color="#FFFFFF"
            active-text-color="#409EFF"
            :collapse-transition="false"
            :collapse="!userStore.isOpenSidebar"
            :style="{ width: userStore.isOpenSidebar ? '200px' : '64px' }"
            :default-active="router.currentRoute.value.path"
          >
            <template v-for="item in userStore.menu">
              <!-- 二级菜单 -->
              <template v-if="item.children.length > 0">
                <el-sub-menu :index="item.path">
                  <template #title>
                    <el-image
                      :style="{ 'margin-right': userStore.isOpenSidebar ? '10px' : '0px' }"
                      :src="IMAGE_URL + item.meta.icon"
                    />
                    <span>{{ item.meta.title }}</span>
                  </template>

                  <template v-for="subItem in item.children">
                    <el-menu-item :index="subItem.path">
                      <el-image
                        :style="{ 'margin-right': userStore.isOpenSidebar ? '10px' : '0px' }"
                        :src="IMAGE_URL + subItem.meta.icon"
                      />
                      <template #title>{{ subItem.meta.title }}</template>
                    </el-menu-item>
                  </template>
                </el-sub-menu>
              </template>

              <!-- 一级菜单 -->
              <template v-else>
                <el-menu-item :index="item.path">
                  <el-image
                    :style="{ 'margin-right': userStore.isOpenSidebar ? '10px' : '0px' }"
                    :src="IMAGE_URL + item.meta.icon"
                  />
                  <template #title>{{ item.meta.title }}</template>
                </el-menu-item>
              </template>
            </template>
          </el-menu>
        </el-aside>

        <el-main>
          <el-breadcrumb separator="/">
            <el-breadcrumb-item v-for="item in router.currentRoute.value.matched" :key="item.path">
              <router-link style="font-weight: 400" :to="{ path: item.path }">{{ item.meta.title }}</router-link>
            </el-breadcrumb-item>
          </el-breadcrumb>

          <el-container class="content">
            <router-view />
          </el-container>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped lang="less">
.layout-page {
  .el-header {
    position: relative;
    color: #ffffff;
    background-color: #242f42;
    padding: 10px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;

    .left {
      display: flex;
      align-items: center;
      font-size: 24px;

      .sidebar-btn {
        display: flex;
      }

      .title {
        margin-left: 20px;
      }
    }

    .right {
    }
  }

  .el-menu {
    height: 100vh;
    background-color: #324157;
    color: #ffffff;

    .el-sub-menu,
    .el-menu-item {
      .el-image {
        width: 20px;
        height: 20px;
        background-color: #adb9c9;
        display: flex;
        align-items: center;
        justify-content: center;
      }
    }
  }

  .el-main {
    margin: 20px;

    .el-breadcrumb {
      font-size: 16px;
      margin-bottom: 20px;
    }

    .content {
      width: 100%;
      height: calc(100% - 60px - 20px - 16px);
      background-color: #dfdcdc;
    }
  }
}

.layout-page .layout-page .el-menu {
  border-right: none;
}

.layout-page .el-main {
  padding: 0;
}

.el-aside {
  transition: width 0.35s;
  -webkit-transition: width 0.35s;
  -moz-transition: width 0.35s;
  -webkit-transition: width 0.35s;
  -o-transition: width 0.35s;
}
</style>
