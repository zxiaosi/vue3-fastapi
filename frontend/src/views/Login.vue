<script setup lang="ts">
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";
import { ElMessage } from "element-plus";
import { User, Lock } from "@element-plus/icons-vue";
import { useStore } from "@/stores";
import { login } from "@/api/login";
import { setLocal } from "@/request/auth";

const router = useRouter();
const param = reactive({
  username: "admin",
  password: "123",
});

const loginRef = ref();

// 用户校验
const loginRules = {
  username: [{ required: true, message: "请输入用户名", trigger: "blur" }],
  password: [{ required: true, message: "请输入密码", trigger: "blur" }],
};

const submitForm = () => {
  loginRef.value.validate(async (valid: any) => {
    if (valid) {
      const { access_token } = await login(param);
      if (access_token) {
        ElMessage.success("登录成功");
        setLocal("username", param.username);
        setLocal("Authorization", access_token);
        router.push("/");
      }
    } else {
      ElMessage.warning("数据验证失败！");
      return false;
    }
  });
};

// 状态管理
const store = useStore();
store.clearTags; // 清空标签
</script>

<template>
  <div class="login-wrap">
    <div class="ms-login">
      <div class="ms-title">学生选课系统</div>
      <el-form :model="param" :rules="loginRules" ref="loginRef" label-width="0px" class="ms-content">
        <el-form-item prop="username">
          <el-input v-model="param.username" placeholder="username">
            <template #prepend>
              <el-button :icon="User" />
            </template>
          </el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input type="password" placeholder="password" v-model="param.password" @keyup.enter="submitForm()">
            <template #prepend>
              <el-button :icon="Lock" />
            </template>
          </el-input>
        </el-form-item>
        <div class="login-btn">
          <el-button type="primary" @click="submitForm()">登录</el-button>
        </div>
        <!-- <p class="login-tips">Tips : 用户名和密码随便填。</p> -->
      </el-form>
    </div>
  </div>
</template>

<style scoped>
.login-wrap {
  position: relative;
  width: 100%;
  height: 100%;
  background-image: url(../assets/img/login-bg.jpg);
  background-size: 100%;
}
.ms-title {
  width: 100%;
  line-height: 50px;
  text-align: center;
  font-size: 20px;
  color: #fff;
  border-bottom: 1px solid #ddd;
}
.ms-login {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 350px;
  margin: -190px 0 0 -175px;
  border-radius: 5px;
  background: rgba(255, 255, 255, 0.3);
  overflow: hidden;
}
.ms-content {
  padding: 30px 30px;
}
.login-btn {
  text-align: center;
}
.login-btn button {
  width: 100%;
  height: 36px;
  margin-bottom: 10px;
}
.login-tips {
  font-size: 12px;
  line-height: 30px;
  color: #fff;
}
</style>
