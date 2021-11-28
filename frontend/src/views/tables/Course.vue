<template>
  <div>
    <header-name :iconName='iconName' :pageName='pageName' />

    <!-- 表格 -->
    <div class="container">
      <!-- 排序和添加 -->
      <header-handle :query="query" :data="courseData" :form-data="formData"
        @isAddDialog='isAddDialog' />

      <!-- 表格信息 -->
      <el-table
        :data="courseData.slice((query.pageIndex-1)*(query.pageSize),(query.pageIndex)*(query.pageSize))"
        border class="table" ref="multipleTable" header-cell-class-name="table-header">
        <el-table-column type="index" width="80" label="序号" align="center">
          <template #default="scope">
            <span>{{scope.$index+((query.pageIndex) - 1) * (query.pageSize) + 1}} </span>
          </template>
        </el-table-column>

        <el-table-column prop="id" label="课程编号" align="center" />
        <el-table-column prop="name" label="课程名字" align="center" />
        <el-table-column prop="credit" label="学分" align="center" />
        <el-table-column prop="period" label="课时" align="center" />

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
    <el-dialog :title="`${addOrUpdate ? '添加课程信息' : '编辑课程信息'}`" v-model="showDialog" width="30%">
      <el-form label-width="100px" ref="formRef" :model="formData" :rules="formRules"
        autocomplete="on">
        <el-form-item label="课程编号" prop="id">
          <el-input v-model="formData.id" placeholder="编号" :disabled=!addOrUpdate></el-input>
        </el-form-item>
        <el-form-item label="课程名字" prop="name">
          <el-input v-model="formData.name" placeholder="名字"></el-input>
        </el-form-item>
        <el-form-item label="学分" prop="credit">
          <el-input v-model="formData.credit" placeholder="学分"></el-input>
        </el-form-item>
        <el-form-item label="课时" prop="period">
          <el-input v-model="formData.period" placeholder="课时"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="showDialog = false">取 消</el-button>
          <el-button type="primary" v-if="addOrUpdate" @click="saveAdd">添 加</el-button>
          <el-button type="primary" v-else @click="saveEdit">更 新</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, watchEffect } from 'vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import { Edit, Delete } from '@element-plus/icons'; // 图标
import HeaderName from '../../components/tables/HeaderName.vue';
import HeaderHandle from '../../components/tables/HeaderHandle.vue';
import {
  read_courses,
  create_course,
  update_course,
  delete_course,
} from '../../api/course';

// 定义icon和页面名字
const iconName = ref('cascades');
const pageName = ref('课程表');

const courseData = ref([]); // 数据变量
const pageTotal = ref(0); // 总个数

/**
 * getData()
 * 获取表格数据
 */
const getData = () => {
  read_courses(query)
    .then((res) => {
      courseData.value = res.data;
    })
    .catch(() => {
      ElMessage.error('加载课程信息数据失败');
    });
};

// 页面加载后调用函数
onMounted(() => {
  getData();
});

// 监听属性
watchEffect(() => {
  pageTotal.value = courseData.value.length || 10;
});

// 排序和页码
const query = reactive({
  sort: 'up',
  pageIndex: 1,
  pageSize: 10,
});

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
const isAddDialog = (res) => {
  addOrUpdate.value = res;
  showDialog.value = res;
};

const formRef = ref();

// 定义校验规则
const formRules = reactive({
  id: [
    {
      required: 'true',
      pattern: /^[1-9]/,
      message: '请输入课程编号(以1-9开头)',
      trigger: 'change',
    },
    {
      min: 4,
      max: 4,
      message: '课程编号的长度应为4',
    },
  ],
  name: [
    {
      required: 'true',
      message: '请输入课程名称',
      trigger: ['change', 'blur'],
    },
  ],
  credit: [
    {
      required: 'true',
      message: '请输入学时',
      trigger: ['change', 'blur'],
    },
  ],
  period: [
    {
      required: 'true',
      message: '请输入学分',
      trigger: ['change', 'blur'],
    },
  ],
});

// 表单对象
const formData = reactive({
  id: '',
  name: '',
  credit: '',
  period: '',
});

let idx = -1; // 课程ID
let reIndex = -1; // 序号

/**
 * saveAdd
 * 确认添加
 */
const saveAdd = () => {
  showDialog.value = false;
  formRef.value.validate((valid) => {
    if (valid) {
      create_course(formData)
        .then((res) => {
          courseData.value.push(res.data);
          ElMessage.success('成功添加课程信息！');
        })
        .catch(() => {
          ElMessage.error('添加课程信息失败！');
        });
    } else {
      ElMessage.warning('课程信息填写有误，添加失败！');
    }
    // 重置表单
    formRef.value.resetFields();
  });
};

/**
 * handleEdit
 * 编辑课程信息
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
      update_course(idx, formData)
        .then((res) => {
          ElMessage.success(`修改课程ID为 ${idx} 成功！`);
          Object.keys(res.data).forEach((item) => {
            courseData.value[reIndex][item] = res.data[item];
          });
        })
        .catch((error) => {
          ElMessage.error('修改课程信息失败！');
          console.log(error);
        });
    } else {
      ElMessage.warning('填写课程信息有误，修改失败！');
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
      // 调用删除课程接口
      delete_course(idx)
        .then(() => {
          courseData.value.splice(index, 1);
          ElMessage.success('删除成功！');
        })
        .catch(function (error) {
          ElMessage.success('删除成功！');
        });
    })
    .catch(() => {});
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