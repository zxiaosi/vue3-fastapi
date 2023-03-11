<script setup lang="ts">
import { getLangList } from "@/apis";
import { useUserStore } from "@/stores";
import { onMounted, onUnmounted } from "vue";
import * as echarts from "echarts"; // 引入echarts
import { getLocal } from "@/request/auth";

let chart: any;

const userStore = useUserStore();
const _user = getLocal("userInfo") || userStore.user;

onMounted(async () => {
  const { data } = await getLangList();
  const obj = processData(data);

  // @ts-ignore
  chart = echarts.init(document.getElementById("line"));
  eachartConfig(obj);
});

// 销毁echarts
onUnmounted(() => {
  chart?.dispose();
});

/**
 * echarts-bar(柱状图)
 */
const eachartConfig = (data: any) => {
  chart.setOption({
    title: { text: "提交次数", left: "center" },
    legend: { show: true },
    tooltip: { trigger: "item", formatter: "{b} : commit {c} 次" },
    xAxis: { type: "category", data: Object.keys(data) },
    yAxis: { type: "value" },
    series: [{ type: "line", data: Object.values(data) }],
  });
  // 自适应
  window.onresize = function () {
    chart.resize();
  };
};

/**
 * 统计从 new Date("2021-09") 到 new("2023-03") 每个月的提交次数
 */
const processData = (data: any) => {
  const obj = {} as any;

  const start = new Date("2021-09");
  const end = new Date("2023-03");

  while (start <= end) {
    const year = start.getFullYear();
    const month = start.getMonth() + 1;
    const date = `${year}-${month < 10 ? "0" + month : month}`;
    const count = data.filter((item: any) => item.commit.author.date.slice(0, 7) == date).length;
    obj[date] = count;
    start.setMonth(month);
  }

  return obj;
};
</script>

<template>
  <el-card class="card-left" shadow="hover">
    <template #header>
      <div class="card-header">用户信息</div>
    </template>
    <ul class="user-info">
      <li>
        <el-image src="https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg" />
      </li>
      <li>
        <div class="key">用户名称</div>
        <div class="value">{{ _user.name }}</div>
      </li>
      <li>
        <div class="key">用户性别</div>
        <div class="value">{{ _user.sex == 0 ? "保密" : _user.sex == 1 ? "男" : "女" }}</div>
      </li>
    </ul>
  </el-card>

  <el-card class="card-right" shadow="hover">
    <template #header>
      <div class="card-header">代码仓库</div>
    </template>
    <div id="line"></div>
  </el-card>
</template>

<style scoped lang="less">
.card-left {
  width: 500px;

  .user-info {
    list-style: none;

    li {
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 20px;

      .el-image {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 1px solid #ccc;
      }

      .key {
        margin-right: 20px;
      }
    }

    li:nth-child(2) {
      border-top: 2px dashed #ccc;
      padding-top: 20px;
    }
  }
}

.card-right {
  flex: 1;

  .card-header {
    display: flex;
    align-items: center;

    span {
      margin-right: 20px;
    }
  }

  #line {
    width: 100%;
    height: 80vh;
  }
}
</style>
