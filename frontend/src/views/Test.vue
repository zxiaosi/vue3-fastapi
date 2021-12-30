<template>
  <div>
    <header-name :iconName='iconName' :pageName='pageName' />

    <div class="container">
      <div class="plugins-tips">测试用户信息表格</div>

      <!-- 排序和添加 -->
      <!-- <header-handle :query="query" :data="tableData" :form-data="formData"
        @isAddDialog='isAddDialog' /> -->

      <!-- 表格信息 -->
      <el-table
        :data="tableData.slice((query.currentPage-1)*(query.pageSize),(query.currentPage)*(query.pageSize))"
        border class="table" ref="multipleTable" header-cell-class-name="table-header"
        @selection-change="handleSelectionChange">

        <el-table-column type="selection" width="80" align="center" />

        <el-table-column type="index" width="55" label="序号" align="center">
          <template #default="scope">
            <span>{{scope.$index+((query.currentPage) - 1) * (query.pageSize) + 1}} </span>
          </template>
        </el-table-column>

        <el-table-column prop="id" label="用户ID" width="80" align="center"></el-table-column>
        <el-table-column prop="full_name" label="用户名"></el-table-column>

        <!-- 操作 -->
        <el-table-column label="操作" width="180" align="center">
          <template #default="scope">
            <el-button type="text" :icon="Edit" @click="handleEdit(scope.$index, scope.row)">
              编辑
            </el-button>
            <el-button type="text" :icon="Delete" class="red"
              @click="handleDelete(scope.$index, scope.row)">删除
            </el-button>
          </template>
        </el-table-column>

      </el-table>

      <!-- 页码 -->
      <pagination :page-size="query.pageSize" :page-total="pageTotal"
        :current-page="query.currentPage" :render='getData' />
    </div>

    <!-- 编辑弹出框 -->
    <el-dialog :title="`${addOrUpdate ? '添加用户' : '编辑用户'}`" v-model="showDialog" width="30%">
      <el-form label-width="70px" ref="formRef" :model="formData" :rules="formRules"
        autocomplete="on">
        <el-form-item label="用户ID" prop="id">
          <el-input v-model="formData.id" type="number" placeholder="用户ID"></el-input>
        </el-form-item>
        <el-form-item label="用户名" prop="full_name">
          <el-input v-model="formData.full_name" placeholder="用户名"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="formData.password" type="password" placeholder="用户密码"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="showDialog = false">取 消</el-button>
          <el-button type="primary" v-if="addOrUpdate" @click="addUser">添 加</el-button>
          <el-button type="primary" v-else @click="saveEdit">更 新</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, watch } from 'vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import { Edit, Delete } from '@element-plus/icons'; // 图标
import HeaderName from '@components/tables/PageName.vue';
import Pagination from '@components/tables/Pagination.vue';
import { userData, delele_User, update_User, add_User } from '@api/baseTable';

const iconName = ref('test');
const pageName = ref('测试页面');

// 搜索
const query = reactive({
  id: '',
  full_name: '',
  currentPage: 1,
  pageSize: 10,
  sort: 'up',
});
const tableData = ref([]);
const pageTotal = ref(0);

// 获取表格数据
const getData = () => {
  userData(query)
    .then((res) => {
      tableData.value = res;
    })
    .catch(() => {
      ElMessage.warning('加载数据失败！');
    });
  // console.log("我是tableData--", tableData);
};

// 页面加载后调用函数
onMounted(() => {
  getData();
});

// 监听属性
watch(
  () => tableData.value.length,
  (newVal, oldVar) => {
    pageTotal.value = newVal || query.pageSize;
  }
);

// 表格编辑时弹窗和保存
const showDialog = ref(false); // 是否显示弹窗
const addOrUpdate = ref(true); // 是否是添加或更新
const isAddDialog = (res) => {
  addOrUpdate.value = res;
  showDialog.value = res;
};

const formRef = ref(); //
const formData = reactive({
  id: '',
  full_name: '',
  password: '',
});
// 定义校验规则
const formRules = reactive({
  id: [{ required: 'true', message: '请输入用户ID', trigger: 'change' }],
  full_name: [{ required: 'true', message: '请输入用户名', trigger: 'change' }],
  password: [
    { required: 'true', message: '请输入登录密码', trigger: 'change' },
  ],
});
let idx = -1; // 用户ID
let reIndex = -1; // 序号

const addUser = () => {
  showDialog.value = false;
  formRef.value.validate((valid) => {
    if (valid) {
      add_User(formData)
        .then((res) => {
          tableData.value.push(res);
          ElMessage.success('成功添加用户信息！');
        })
        .catch(function (error) {
          ElMessage.warning('添加用户信息失败！');
          console.log(error);
        });
    }
    formRef.value.resetFields();
  });
};

// 编辑用户信息
const handleEdit = (index, row) => {
  idx = row.id;
  reIndex = index;
  Object.keys(formData).forEach((item) => {
    formData[item] = row[item];
  });

  // 显示弹窗(更新)
  addOrUpdate.value = false;
  showDialog.value = true;
};
const saveEdit = () => {
  addOrUpdate.value = false;
  update_User(idx, formData)
    .then(() => {
      ElMessage.success(`修改ID为 ${idx} 成功！`);
      Object.keys(formData).forEach((item) => {
        tableData.value[reIndex][item] = formData[item];
      });
    })
    .catch(function (error) {
      ElMessage.success(`修改ID为 ${idx} 行失败！`);
      console.log(error);
    });
  showDialog.value = false;
};

// 删除操作
const handleDelete = (index, row) => {
  idx = row.id;
  // 二次确认删除
  ElMessageBox.confirm('确定要删除吗？', '提示', {
    type: 'warning',
  })
    .then(() => {
      // 调用删除用户接口
      delele_User(idx)
        .then(() => {
          tableData.value.splice(index, 1);
          ElMessage.success('删除成功！');
        })
        .catch(function (error) {
          ElMessage.success('删除成功！');
          console.log(error);
        });
    })
    .catch(() => {});
};

const handleSelectionChange = (val) => {
  console.log('handleSelectionChange--', val);
  val.map((item) => {
    console.log(item.id);
    tableIdList.value.push(item.id);
  });
};
</script>

<style scoped>
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