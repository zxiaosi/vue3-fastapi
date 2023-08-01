<script setup lang="ts">
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import type { FormInstance, FormRules } from "element-plus";
import { User, Lock } from "@element-plus/icons-vue";
import { userLogin, userSignUp } from "@/apis/index";
import { encryptContent } from "@/utils/encryption";
import { useUserStore } from "@/stores";
import { setLocal } from "@/request/auth";

const router = useRouter();
const userStore = useUserStore();

// 表单实例
const loginRef = ref<FormInstance>();

// 用户信息
const userInfo = reactive({
  name: "admin",
  password: "123456",
});

// 表单校验规则
const loginRules = reactive<FormRules>({
  name: [{ required: true, message: "请输入用户名", trigger: "blur" }],
  password: [{ required: true, message: "请输入密码", trigger: "blur" }],
});

/** 提交表单 */
const submitForm = async (formEl: FormInstance | undefined, type: "login" | "signup") => {
  if (!formEl) return;

  await formEl.validate(async (valid, fields) => {
    if (valid) {
      let params = { name: userInfo.name, password: encryptContent(userInfo.password) };

      let resp: any;
      type == "login" &&
        ({
          data: { data: resp },
        } = await userLogin(params));
      type == "signup" &&
        ({
          data: { data: resp },
        } = await userSignUp(params));
      userStore.user = resp;
      setLocal("userInfo", resp);

      router.push("/");
    } else {
      ElMessage.warning("数据校验失败!");
      console.log("error submit!", fields);
    }
  });
};
</script>

<template>
  <div class="page">
    <div class="card">
      <div class="title">Demo</div>

      <el-form ref="loginRef" :model="userInfo" :rules="loginRules" label-width="0px" class="content">
        <el-form-item prop="name">
          <el-input v-model="userInfo.name" placeholder="用户名" maxlength="20">
            <template #prepend>
              <el-button :icon="User" />
            </template>
          </el-input>
        </el-form-item>

        <el-form-item prop="password">
          <el-input type="password" placeholder="密码" v-model="userInfo.password" show-password maxlength="32">
            <template #prepend>
              <el-button :icon="Lock" />
            </template>
          </el-input>
        </el-form-item>
      </el-form>

      <div class="btn">
        <el-button type="success" @click="submitForm(loginRef, 'signup')">注册</el-button>
        <el-button type="primary" @click="submitForm(loginRef, 'login')">登录</el-button>
      </div>
    </div>
  </div>
</template>

<style scoped lang="less">
.page {
  position: relative;
  width: 100%;
  height: 100%;
  /* 每日一图 */
  background-image: url(https://open.saintic.com/api/bingPic);
  background-size: 100%;

  .card {
    width: 350px;
    border-radius: 5px;
    background: rgba(255, 255, 255, 0.4);
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);

    .title {
      height: 50px;
      line-height: 50px;
      text-align: center;
      font-size: 20px;
      color: #fff;
      border-bottom: 1px solid #ddd;
    }

    .content {
      padding: 30px 30px 0px;
    }

    .btn {
      text-align: center;
      padding-bottom: 30px;
    }
  }
}
</style>
