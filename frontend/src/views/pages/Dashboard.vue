<script setup lang="ts">
import { getLangList } from "@/apis";
import { useUserStore } from "@/stores";
import { onMounted, onUnmounted } from "vue";
import * as echarts from "echarts"; // 引入echarts
import { getLocal } from "@/request/auth";

let chart: any;

const userStore = useUserStore();
const _user = getLocal("userInfo") || userStore.user;

let echartDatas = {}

onMounted(async () => {
  let pages = [1, 2, 3]
  await Promise.all(pages.map((item) => {
    return (async () => {
      const { data } = await getLangList(item)
      const obj = processData(data, getCommitDate(data[data.length - 1]), getCommitDate(data[0]));
      echartDatas = { ...obj, ...echartDatas }
    })()
  }))

  // @ts-ignore
  chart = echarts.init(document.getElementById("line"));
  eachartConfig();
});

// 销毁echarts
onUnmounted(() => {
  chart?.dispose();
});

/**
 * echarts-bar(柱状图)
 */
const eachartConfig = () => {
  chart.setOption({
    title: { text: "提交次数", left: "center" },
    legend: { show: true },
    tooltip: { trigger: "item", formatter: "{b} : commit {c} 次" },
    xAxis: { type: "category", data: Object.keys(echartDatas) },
    yAxis: { type: "value" },
    series: [{ type: "line", data: Object.values(echartDatas) }],
  });
  // 自适应
  window.onresize = function () {
    chart.resize();
  };
};

/**
 * 统计从 startDate 到 endDate 每个月的提交次数 eg: new Date("2021-09") new("2023-03")
 * @param data 遍历的数据
 * @param startDate 开始时间
 * @param endDate 结束时间
 */
const processData = (data: any, startDate: string, endDate: string) => {
  const obj = {} as any;

  const start = new Date(startDate);
  const end = new Date(endDate);

  do {
    const year = start.getFullYear();
    const month = start.getMonth() + 1;
    const date = `${year}-${month < 10 ? "0" + month : month}`;
    const count = data.filter((item: any) => getCommitDate(item) == date).length;
    obj[date] = count;
    start.setMonth(month);
  } while (start <= end);

  return obj;
};

/** 获取提交日志中的时间 */
const getCommitDate = (data: any) => {
  return data.commit.author.date.slice(0, 7);
};
</script>

<template>
  <div class="pages">
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
  </div>
</template>

<style scoped lang="less">
.pages {
  display: flex;

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
    }

    #line {
      width: 100%;
      height: 80vh;
    }
  }
}
</style>
