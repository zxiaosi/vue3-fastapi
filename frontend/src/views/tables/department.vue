<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-ali-cascades"></i> 院系表
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <!-- 表格 -->
    <div class="container">
      <!-- 搜索 -->
      <div class="handle-box">
        <el-select v-model="query.sort" placeholder="排序" class="handle-select mr10">
          <el-option key="1" label="升序" value="up"></el-option>
          <el-option key="2" label="降序" value="down"></el-option>
        </el-select>
        <el-button type="primary"
          :icon="`${query.sort === 'up' ?  'el-icon-sort-up' : 'el-icon-sort-down'}`"
          @click="handleSort">排序
        </el-button>
        <el-button type="primary" icon="el-icon-plus" @click="handleAdd">添加</el-button>
      </div>

      <!-- 表格信息 -->
      <el-table
        :data="deptData.slice((query.pageIndex-1)*(query.pageSize),(query.pageIndex)*(query.pageSize))"
        border class="table" ref="multipleTable" header-cell-class-name="table-header">
        <el-table-column type="index" width="80" label="序号" align="center">
          <template #default="scope">
            <span>{{scope.$index+((query.pageIndex) - 1) * (query.pageSize) + 1}} </span>
          </template>
        </el-table-column>

        <el-table-column prop="id" label="院系编号" width="120" align="center"></el-table-column>
        <el-table-column prop="name" label="院系名字" width="140" align="center"></el-table-column>
        <el-table-column prop="chairman" label="主任名" width="140" align="center"></el-table-column>
        <el-table-column prop="phone" label="主任手机号" align="center"></el-table-column>

        <!-- 操作 -->
        <el-table-column label="操作" width="180" align="center">
          <template #default="scope">
            <el-button type="text" icon="el-icon-edit" @click="handleEdit(scope.$index, scope.row)">
              编辑
            </el-button>
            <el-button type="text" icon="el-icon-delete" class="red"
              @click="handleDelete(scope.$index, scope.row)">删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- 页码 -->
      <div class="pagination">
        <el-pagination background layout="total, sizes, prev, pager, next, jumper"
          :current-page="query.pageIndex" :page-sizes="[10]" :page-size="query.pageSize"
          :total="pageTotal" @size-change="handleSizeChange" @current-change="handlePageChange">
        </el-pagination>
      </div>
    </div>

    <!-- 编辑弹出框 -->
    <el-dialog :title="`${addOrUpdate ? '添加院系信息' : '编辑院系信息'}`" v-model="showDialog" width="30%">
      <el-form label-width="100px" ref="formRef" :model="formData" :rules="formRules"
        autocomplete="on">
        <el-form-item label="院系编号" prop="id">
          <el-input v-model="formData.id" placeholder="编号" :disabled=!addOrUpdate></el-input>
        </el-form-item>
        <el-form-item label="院系名字" prop="name">
          <el-input v-model="formData.name" placeholder="名字"></el-input>
        </el-form-item>
        <el-form-item label="主任名" prop="chairman">
          <el-input v-model="formData.chairman" placeholder="主任名"></el-input>
        </el-form-item>
        <el-form-item label="主任手机号" prop="phone">
          <el-input v-model="formData.phone" type="tel" placeholder="手机号"></el-input>
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
import { ref, reactive, onMounted, watchEffect } from 'vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import {
  read_departments,
  create_department,
  update_department,
  delete_department,
} from '../../api/department';

export default {
  name: 'department',
  setup() {
    const deptData = ref([]); // 数据变量
    const pageTotal = ref(0); // 总个数

    /**
     * getData()
     * 获取表格数据
     */
    const getData = () => {
      read_departments(query)
        .then((res) => {
          deptData.value = res.data;
        })
        .catch(() => {
          ElMessage.error('加载院系信息数据失败');
        });
    };

    // 页面加载后调用函数
    onMounted(() => {
      getData();
    });

    // 监听属性
    watchEffect(() => {
      pageTotal.value = deptData.value.length || 10;
    });

    // 排序和页码
    const query = reactive({
      sort: 'up',
      pageIndex: 1,
      pageSize: 10,
    });

    /**
     * handleSort
     * 升序操作
     */
    const handleSort = (event) => {
      clickRecover(event);

      if (query.sort === 'up') {
        deptData.value.sort((a, b) => a.id - b.id);
      } else {
        deptData.value.sort((a, b) => b.id - a.id);
      }
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

    // 添加、编辑表格的弹窗和保存
    const showDialog = ref(false); // 是否显示弹窗
    const addOrUpdate = ref(true); // 是否是添加或更新
    const formRef = ref();

    // 定义校验规则
    const formRules = reactive({
      id: [
        {
          required: 'true',
          pattern: /^10[0-9]{2}/,
          message: '请输入院系编号(以10开头)',
          trigger: 'change',
        },
        {
          min: 4,
          max: 4,
          message: '院系编号的长度应为4',
        },
      ],
      name: [
        {
          required: 'true',
          message: '请输入院系名称',
          trigger: ['change', 'blur'],
        },
      ],
      chairman: [
        {
          required: 'true',
          message: '请输入院系主任名', // 后台字段默认最多能输入10个汉字
          trigger: ['change', 'blur'],
        },
        {
          max: 4,
          message: '主任名长度不能超过4',
        },
      ],
      phone: [
        {
          pattern: /^((0\d{2,3}-\d{7,8})|(1[34578]\d{9}))$/,
          message: '请输入正确的手机号',
          trigger: ['change', 'blur'],
        },
      ],
    });

    // 表单对象
    const formData = reactive({
      id: '',
      name: '',
      chairman: '',
      phone: '',
    });

    let idx = -1; // 院系ID
    let reIndex = -1; // 序号

    /**
     * handleAdd
     * 添加院系信息
     */
    const handleAdd = (event) => {
      clickRecover(event);

      // 重置表单(防止编辑页面数据)
      Object.keys(formData).forEach((key) => (formData[key] = ''));

      // 显示弹窗(添加)
      addOrUpdate.value = true;
      showDialog.value = true;
    };
    /**
     * addUser
     * 确认添加
     */
    const addUser = () => {
      showDialog.value = false;
      formRef.value.validate((valid) => {
        if (valid) {
          create_department(formData)
            .then((res) => {
              deptData.value.push(res.data);
              ElMessage.success('成功添加院系信息！');
            })
            .catch(() => {
              ElMessage.error('添加院系信息失败！');
            });
        } else {
          ElMessage.warning('院系信息填写有误，添加失败！');
        }
        // 重置表单
        formRef.value.resetFields();
      });
    };

    /**
     * handleEdit
     * 编辑院系信息
     */
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
    /**
     * saveEdit
     * 确认更新
     */
    const saveEdit = () => {
      addOrUpdate.value = false;
      showDialog.value = false;

      formRef.value.validate((valid) => {
        if (valid) {
          update_department(idx, formData)
            .then((res) => {
              ElMessage.success(`修改院系ID为 ${idx} 成功！`);
              Object.keys(res.data).forEach((item) => {
                deptData.value[reIndex][item] = res.data[item];
              });
            })
            .catch((error) => {
              ElMessage.error('修改院系信息失败！');
              console.log(error);
            });
        } else {
          ElMessage.warning('填写院系信息有误，修改失败！');
        }
      });
    };

    /**
     * handleDelete
     * 删除操作
     */
    const handleDelete = (index, row) => {
      idx = row.id;
      // 二次确认删除
      ElMessageBox.confirm('确定要删除吗？', '提示', {
        type: 'warning',
      })
        .then(() => {
          // 调用删除院系接口
          delete_department(idx)
            .then(() => {
              deptData.value.splice(index, 1);
              ElMessage.success('删除成功！');
            })
            .catch(function (error) {
              ElMessage.success('删除成功！');
            });
        })
        .catch(() => {});
    };

    /**
     * clickRecover
     * 点击后鼠标移开恢复按钮默认样式
     */
    const clickRecover = (event) => {
      let target = event.target;
      // (如果按钮没有加icon图标的话，target.nodeName == "I"可以去掉)
      if (target.nodeName == 'I' || target.nodeName == 'SPAN') {
        target = event.target.parentNode;
      }
      target.blur();
    };

    // 返回
    return {
      query,
      deptData,
      pageTotal,
      showDialog,
      addOrUpdate,
      formRef,
      formData,
      formRules,
      handleSort,
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