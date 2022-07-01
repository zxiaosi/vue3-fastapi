<script setup lang="ts">
import { reactive, onMounted } from "vue";
import { Clock } from "@element-plus/icons-vue";
import { getUserInfo, readData } from "@/api";
import { getLocal, setLocal } from "@/request/auth";
import { dateFunction } from "@/utils/handleTime";
import { PathEnum } from "@/types/table";
import { type UserInfo, type State, SexEnum, EduEnum, TitleEnum } from ".";

let userInfo: UserInfo = reactive({});

const state: State = reactive({
  role: "",
  foreignKeyName: "",
  details: [],
});

onMounted(async () => {
  let role = getLocal("role");
  state.role = role;
  const data = await getUser(role); // 请求接口
  await processData(role, data); // 处理数据
});

/**
 * 获取用户信息
 */
const getUser = async (role: any) => {
  const { data } = await getUserInfo({ roles: role });
  Object.assign(userInfo, data);
  setLocal("userInfo", JSON.stringify(data));
  return data;
};

/**
 * 加工数据(感觉权限返回不同用户的信息)
 */
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
      const { data: dept } = await readData({ path: PathEnum.dept, id: data.departmentId });
      state.details = [
        { text: "头像", value: data.image },
        { text: "职工号", value: data.id },
        { text: "性别", value: SexEnum[data.sex] },
        { text: "生日", value: data.birthday },
        { text: "学历", value: EduEnum[data.education] },
        { text: "职称", value: TitleEnum[data.title] },
        { text: "院系编号", value: dept.name },
        { text: "上次登录地点", value: data.address },
      ];
      break;
    case "student":
      const { data: major } = await readData({ path: PathEnum.major, id: data.majorId });
      state.details = [
        { text: "头像", value: data.image },
        { text: "学号", value: data.id },
        { text: "性别", value: SexEnum[data.sex] },
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
