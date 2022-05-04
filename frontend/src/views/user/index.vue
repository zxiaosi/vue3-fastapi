<script setup lang="ts">
import { reactive, onMounted } from "vue";
import { get_current_user, read_data } from "@/api";
import { getLocal, setLocal } from "@/request/auth";
import { Clock } from "@element-plus/icons-vue";
import { dateFunction } from "../../utils/handleTime";
import { pathEnum } from "@/types/table";

// 性别枚举
const sexEnum = {
  "0": "男",
  "1": "女",
};

// 学历枚举
const eduEnum = {
  "1": "学士",
  "2": "硕士",
  "3": "博士",
};

// 职称枚举
const titleEnum = {
  "1": "助教",
  "2": "讲师",
  "3": "副教授",
  "4": "教授",
};

let userInfo: UserInfo = reactive({});

const state = reactive({
  role: "",
  foreignKeyName: "",
  details: [] as Details[],
});

onMounted(async () => {
  let role = getLocal("role");
  state.role = role;
  const data = await getUserInfo(role); // 请求接口
  await processData(role, data); // 处理数据
  console.log("userInfo--", userInfo);
});

/**
 * 获取用户信息
 */
const getUserInfo = async (role: any) => {
  const { data } = await get_current_user({ roles: role });
  Object.assign(userInfo, data);
  console.log(data);
  setLocal("userInfo", JSON.stringify(data));
  return data;
};

const processData = async (role: string, data: any) => {
  switch (role) {
    case "admin":
      state.details = [
        { text: "头像", value: userInfo.image },
        { text: "编号", value: userInfo.id },
        { text: "上次登录地点", value: data.address },
      ];
      break;
    case "teacher":
      const { data: dept } = await read_data({ path: pathEnum.dept, id: data.department_id });
      state.details = [
        { text: "头像", value: data.image },
        { text: "职工号", value: data.id },
        { text: "性别", value: sexEnum[data.sex] },
        { text: "生日", value: data.birthday },
        { text: "学历", value: eduEnum[data.education] },
        { text: "职称", value: titleEnum[data.title] },
        { text: "院系编号", value: dept.name },
        { text: "上次登录地点", value: data.address },
      ];
      break;
    case "student":
      const { data: major } = await read_data({ path: pathEnum.major, id: data.major_id });
      state.details = [
        { text: "头像", value: data.image },
        { text: "学号", value: data.id },
        { text: "性别", value: sexEnum[data.sex] },
        { text: "生日", value: data.birthday },
        { text: "专业编号", value: major.name },
        { text: "上次登录地点", value: data.address },
      ];
      break;
    default:
      break;
  }
};
</script>

<template>
  <div>
    <el-card shadow="hover">
      <template #header>
        <div class="clearfix"><span>基础信息</span></div>
      </template>

      <div class="info">
        <div class="info-name">{{ userInfo.name }} - {{ state.role == "admin" ? "超级管理员" : "普通用户" }}</div>
        <div class="info-time">
          注册时间：<el-icon><clock /></el-icon>&nbsp;{{ dateFunction(userInfo.create_time) }}
        </div>
        <div class="info-time">
          修改时间：<el-icon><clock /></el-icon>&nbsp;{{ dateFunction(userInfo.update_time) }}
        </div>

        <div style="border-bottom: 1px solid #e6e6e6" />

        <template v-for="info in state.details">
          <div class="info-div">
            <span>{{ info.text }}</span>
            <img v-if="info.text == '头像'" :src="info.value" width="40" height="40" />
            <span v-else>{{ info.value }}</span>
          </div>
        </template>
      </div>
    </el-card>
  </div>
</template>

<style scoped>
.info {
  text-align: center;
  padding: 0px 0 10px;
}
.info-name {
  margin: 15px 0 10px;
  font-size: 24px;
  font-weight: 500;
  color: #262626;
}

.info-time {
  margin: 15px 0 10px;
  font-size: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.info-div {
  font-size: 16px;
  padding: 10px 35% 0px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>
