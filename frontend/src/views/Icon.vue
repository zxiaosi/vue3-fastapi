<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-ali-emoji"></i> 自定义图标
                </el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <h2>使用方法</h2>
            <p style="line-height: 50px;">直接通过设置类名为 el-icon-ali-iconName 来使用即可。例如：（共{{iconList.length}}个图标）</p>
            <p class="example-p">
                <i class="el-icon-ali-test" style="font-size: 30px;color: #ff5900"></i>
                <span>&lt;i class=&quot;el-icon-ali-test&quot;&gt;&lt;/i&gt;</span>
            </p>
            <p class="example-p">
                <i class="el-icon-ali-weibo" style="font-size: 30px;color:#fd5656"></i>
                <span>&lt;i class=&quot;el-icon-ali-weibo&quot;&gt;&lt;/i&gt;</span>
            </p>
            <p class="example-p">
                <i class="el-icon-ali-emojifill" style="font-size: 30px;color: #ffc300"></i>
                <span>&lt;i class=&quot;el-icon-ali-emojifill&quot;&gt;&lt;/i&gt;</span>
            </p>
            <br />
            <h2>图标</h2>
            <div class="search-box">
                <el-input class="search" size="large" v-model="keyword" clearable placeholder="请输入图标名称"></el-input>
            </div>
            <ul>
                <li class="icon-li" v-for="(item,index) in list" :key="index">
                    <div class="icon-li-content">
                        <i :class="`el-icon-ali-${item}`"></i>
                        <span>{{item}}</span>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import { computed, ref } from "vue";
export default {
    name: "icon",
    setup() {
        const iconList = [
            "emojifill",
            "weibo",
            "camerafill",
            "test",
            "warn",
            "copy",
            "calendar",
            "global",
            "emoji",
            "cascades",
            "home",
        ];
        const keyword = ref("");
        const list = computed(() => {
            return iconList.filter((item) => {
                return item.indexOf(keyword.value) !== -1;
            });
        });

        return {
            iconList,
            keyword,
            list,
        };
    },
};
</script>

<style scoped>
.example-p {
    height: 45px;
    display: flex;
    align-items: center;
}
.search-box {
    text-align: center;
    margin-top: 10px;
}
.search {
    width: 300px;
}
ul,
li {
    list-style: none;
}
.icon-li {
    display: inline-block;
    padding: 10px;
    width: 120px;
    height: 120px;
}
.icon-li-content {
    display: flex;
    height: 100%;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}
.icon-li-content i {
    font-size: 36px;
    color: #606266;
}
.icon-li-content span {
    margin-top: 10px;
    color: #787878;
}
</style>