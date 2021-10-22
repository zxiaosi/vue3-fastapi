<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-ali-test"></i> 测试页面
                </el-breadcrumb-item>
            </el-breadcrumb>
        </div>

        <div class="container">
            <div class="plugins-tips">测试用户信息表格</div>
            <el-table :data="tableData" border class="table" ref="multipleTable" header-cell-class-name="table-header">
                <el-table-column prop="id" label="ID" width="55" align="center"></el-table-column>
                <el-table-column prop="full_name" label="用户名"></el-table-column>
            </el-table>
        </div>
    </div>
</template>

<script>
import { ref } from "vue";
import {userData} from "../api/index"
export default {
    name: "donate",
    setup() {
        // 定义
        const tableData = ref([]);

        // 获取表格数据
        const getData = () => {
            userData().then((res) => {
                tableData.value = res;
            });
        }
        getData();

        // 返回
        return {tableData}
    }
};
</script>

<style>
.handle-box {
    margin-bottom: 20px;
}

.handle-select {
    width: 120px;
}

.handle-input {
    width: 300px;
    display: inline-block;
}
.table {
    width: 100%;
    font-size: 14px;
}
.red {
    color: #ff0000;
}
.mr10 {
    margin-right: 10px;
}
.table-td-thumb {
    display: block;
    margin: auto;
    width: 40px;
    height: 40px;
}
</style>