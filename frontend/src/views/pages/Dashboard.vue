<script setup lang="ts">
import { getLangList } from "@/apis";
import { useUserStore } from "@/stores";
import { computed, onMounted, onUnmounted } from "vue";
import * as echarts from "echarts"; // 引入echarts
import MyUpload from "@/components/MyUpload.vue";
import { IMAGE_URL } from "@/assets/js/global";

let chart: any;

const userStore = useUserStore();
const userInfo = computed(() => userStore.user);

let echartDatas = {};

onMounted(async () => {
  let pages = [1, 2, 3];
  const [data1, data2, data3] = await Promise.all(
    pages.map((item) => {
      return (async () => {
        const { data } = await getLangList(item);
        const obj = processData(data, getCommitDate(data[data.length - 1]), getCommitDate(data[0]));
        return obj;
      })();
    })
  );
  echartDatas = { ...data3, ...data2, ...data1 };

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
          <el-image v-if="userInfo.avatar" :src="IMAGE_URL + userInfo.avatar" />
          <el-image v-else src="https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg" />
        </li>
        <li>
          <div class="key">用户名称</div>
          <div class="value">{{ userInfo.name }}</div>
        </li>
        <li>
          <div class="key">用户性别</div>
          <div class="value">{{ userInfo.sex == 0 ? "保密" : userInfo.sex == 1 ? "男" : "女" }}</div>
        </li>
        <li>
          <div class="key">用户角色</div>
          <div class="value">{{ userInfo.role_name }}</div>
        </li>
      </ul>

      <MyUpload />
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
      height: 74vh;
    }
  }
}
</style>
