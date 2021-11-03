<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-ali-test"></i> 用户表
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="container">
      <div class="plugins-tips">测试用户信息表格</div>

      <!-- 搜索 -->
      <div class="handle-box">
        <el-select v-model="query.id" placeholder="ID" class="handle-select mr10">
          <el-option key="1" label="测试1" value="1"></el-option>
          <el-option key="2" label="测试2" value="2"></el-option>
        </el-select>
        <el-input v-model="query.full_name" placeholder="用户名" class="handle-input mr10"></el-input>
        <el-button type="primary" icon="el-icon-search" @click="handleSearch" disabled>搜索</el-button>
        <el-button type="primary" icon="el-icon-plus" @click="handleAdd">添加</el-button>
      </div>

      <!-- 表格信息 -->
      <el-table :data="tableData.slice((query.pageIndex-1)*(query.pageSize),(query.pageIndex)*(query.pageSize))" border class="table" ref="multipleTable" header-cell-class-name="table-header">
        <el-table-column type="index" width="55" label="序号" align="center">
          <template #default="scope">
            <span>{{scope.$index+((query.pageIndex) - 1) * (query.pageSize) + 1}} </span>
          </template>
        </el-table-column>

        <el-table-column prop="id" label="用户ID" width="80" align="center"></el-table-column>
        <el-table-column prop="full_name" label="用户名"></el-table-column>

        <!-- 操作 -->
        <el-table-column label="操作" width="180" align="center">
          <template #default="scope">
            <el-button type="text" icon="el-icon-edit" @click="handleEdit(scope.$index, scope.row)">编辑
            </el-button>
            <el-button type="text" icon="el-icon-delete" class="red" @click="handleDelete(scope.$index, scope.row)">删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- 页码 -->
      <div class="pagination">
        <el-pagination background layout="total, sizes, prev, pager, next, jumper" :current-page="query.pageIndex" :page-sizes="[10]" :page-size="query.pageSize" :total="pageTotal" @size-change="handleSizeChange" @current-change="handlePageChange"></el-pagination>
      </div>
    </div>

    <!-- 编辑弹出框 -->
    <el-dialog :title="`${addOrUpdate ? '添加用户' : '编辑用户'}`" v-model="showDialog" width="30%">
      <el-form label-width="70px" ref="formRef" :model="formData" :rules="formRules" autocomplete="on">
        <el-form-item label="用户ID" prop="id">
          <el-input v-model="formData.id" type="number" placeholder="用户ID"></el-input>
        </el-form-item>
        <el-form-item label="用户名" prop="full_name">
          <el-input v-model="formData.full_name" placeholder="用户名"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="formData.password" type="password" placeholder="用户密码" maxlength="20"></el-input>
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

<script>
import { ref, reactive, onMounted, watch } from 'vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import { userData, delele_User, update_User, add_User } from '../../api/index';

export default {
  name: 'users',
  setup() {
    // 搜索
    const query = reactive({
      id: '',
      full_name: '',
      pageIndex: 1,
      pageSize: 10,
    });
    const tableData = ref([]);
    const pageTotal = ref(0);
    // 获取表格数据
    const getData = () => {
      userData(query)
        .then((res) => {
          tableData.value = res;
        })
        .catch(function (error) {
          ElMessage.warning('加载数据失败！');
          console.log(error);
        });
    };

    // 页面加载后调用函数
    onMounted(() => {
      getData();
    });

    // 监听属性
    watch(
      () => tableData.value.length,
      (newVal, oldVar) => {
        pageTotal.value = newVal || 10;
      }
    );

    // 查询操作
    const handleSearch = () => {
      query.pageIndex = 1;
      getData();
    };

    // 分页导航
    const handleSizeChange = (val) => {
      console.log(`每页 ${val} 条`);
    };
    const handlePageChange = (val) => {
      query.pageIndex = val;
      console.log(`当前页: ${val}`);
      getData();
    };

    // 表格编辑时弹窗和保存
    const showDialog = ref(false); // 是否显示弹窗
    const addOrUpdate = ref(true); // 是否是添加或更新
    const formRef = ref(); //
    const formData = reactive({
      id: '',
      full_name: '',
      password: '',
    });
    // 定义校验规则
    const formRules = reactive({
      id: [{ required: 'true', message: '请输入用户ID', trigger: 'blur' }],
      full_name: [
        { required: 'true', message: '请输入用户名', trigger: 'blur' },
      ],
      password: [
        { required: 'true', message: '请输入登录密码', trigger: 'blur' },
      ],
    });
    let idx = -1; // 用户ID
    let reIndex = -1; // 序号

    // 添加用户信息
    const handleAdd = (event) => {
      // 点击后鼠标移开恢复按钮默认样式(如果按钮没有加icon图标的话，target.nodeName == "I"可以去掉)
      let target = event.target;
      if (target.nodeName == 'I' || target.nodeName == 'SPAN') {
        target = event.target.parentNode;
      }
      target.blur();

      // 重置表单
      Object.keys(formData).forEach((key) => (formData[key] = ''));

      // 显示弹窗(添加)
      addOrUpdate.value = true;
      showDialog.value = true;
    };
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
        }else{
        ElMessage.warning('输入用户信息有错,添加失败！');
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
      formRef.value.validate((valid) => {
        if(valid){
          update_User(idx, formData)
            .then(() => {
              ElMessage.success(`修改ID为 ${idx} 成功！`);
              Object.keys(formData).forEach((item) => {
                tableData.value[reIndex][item] = formData[item];
              });
            })
            .catch(function (error) {
              ElMessage.warning(`修改ID为 ${idx} 行失败！`);
              console.log(error);
            });
          showDialog.value = false;
        }else{
          ElMessage.warning("输入用户信息有错,修改失败！");
        }
      })
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

    // 返回
    return {
      query,
      tableData,
      pageTotal,
      showDialog,
      addOrUpdate,
      formRef,
      formData,
      formRules,
      handleSearch,
      handleSizeChange,
      handlePageChange,
      handleAdd,
      addUser,
      handleEdit,
      saveEdit,
      handleDelete,
    };
  },
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