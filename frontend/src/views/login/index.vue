<script setup lang="ts">
import { ref, reactive, watch } from "vue";
import { useRouter } from "vue-router";
import { ElForm, ElMessage, type FormInstance, type FormRules } from "element-plus";
import { User, Lock } from "@element-plus/icons-vue";
import { login } from "@/api/login";
import { setLocal } from "@/request/auth";
import { getUserInfo } from "@/api";
import type { UserNamePwd } from ".";

// 全局路由
const router = useRouter();

// 权限
const roles = ref<"admin" | "teacher" | "student">("admin");

// 用户账号与密码
const userInfo: UserNamePwd = reactive({
  username: "admin",
  password: "123456",
});

watch(roles, (newVal: string, oldVal: string) => {
  switch (newVal) {
    case "admin":
      userInfo.username = "admin";
      userInfo.password = "123456";
      break;
    case "teacher":
      userInfo.username = "陈江川";
      userInfo.password = "123456";
      break;
    case "student":
      userInfo.username = "王芳";
      userInfo.password = "123456";
      break;
  }
});

const loginRef = ref<FormInstance>();

// 数据校验
const loginRules = reactive<FormRules>({
  username: [{ required: true, message: "请输入用户名", trigger: "blur" }],
  password: [{ required: true, message: "请输入密码", trigger: "blur" }],
});

/**
 * 提交表单
 */
const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  await formEl.validate(async (valid: any) => {
    if (valid) {
      const { access_token } = await login({ ...userInfo, scope: [roles.value] });
      setLocal("Authorization", access_token);
      setLocal("role", roles.value);
      ElMessage.success("登录成功");
      const {
        data: { id, name, image, address, update_time },
      } = await getUserInfo({ roles: roles.value });
      setLocal("userInfo", JSON.stringify({ id, name, image, address, update_time }));
      router.push("/");
    } else {
      ElMessage.warning("数据校验失败！");
    }
  });
};
</script>

<template>
  <div class="login-wrap">
    <div class="ms-login">
      <div class="ms-title">学生选课系统</div>
      <el-form ref="loginRef" :model="userInfo" :rules="loginRules" label-width="0px" class="ms-content">
        <el-form-item prop="username">
          <el-input v-model="userInfo.username" placeholder="用户名" maxlength="10">
            <template #prepend>
              <el-button :icon="User" />
            </template>
          </el-input>
        </el-form-item>

        <el-form-item prop="password">
          <el-input type="password" placeholder="密码" v-model="userInfo.password" show-password maxlength="20" @keyup.enter="submitForm(loginRef)">
            <template #prepend>
              <el-button :icon="Lock" />
            </template>
          </el-input>
        </el-form-item>

        <div class="login-btn">
          <el-button type="primary" @click="submitForm(loginRef)">登录</el-button>
        </div>

        <p class="login-tips">
          <el-radio-group v-model="roles">
            <el-radio label="admin">管理员</el-radio>
            <el-radio label="teacher">教师</el-radio>
            <el-radio label="student">学生</el-radio>
          </el-radio-group>
        </p>
      </el-form>
    </div>
  </div>
</template>

<style scoped>
.login-wrap {
  position: relative;
  width: 100%;
  height: 100%;
  /* 每日一图 */
  background-image: url(https://open.saintic.com/api/bingPic/);
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
  text-align: center;
}
</style>
