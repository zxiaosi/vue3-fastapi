<template>
  <div>
    <header-name :iconName='iconName' :pageName='pageName' />

    <!-- 表格 -->
    <div class="container">
      <!-- 排序和添加 -->
      <header-handle :query="query" :data="teacherData" :form-data="formData"
        @isAddDialog='isAddDialog' />

      <!-- 表格信息 -->
      <el-table
        :data="teacherData.slice((query.pageIndex-1)*(query.pageSize),(query.pageIndex)*(query.pageSize))"
        border class="table" ref="multipleTable" header-cell-class-name="table-header">

        <!-- 序号 -->
        <el-table-column type="index" width="80" label="序号" align="center">
          <template #default="scope">
            <span>{{scope.$index+((query.pageIndex) - 1) * (query.pageSize) + 1}} </span>
          </template>
        </el-table-column>

        <el-table-column prop="id" label="职工号" width="120" align="center" />
        <el-table-column prop="name" label="教师名字" width="120" align="center" />
        <el-table-column prop="sex" label="教师性别" width="120" align="center">
          <template #default="scope">
            <el-tag :type="scope.row.sex === 'man' ? 'success': 'danger'">
              {{ scope.row.sex=== 'man' ? '男': '女' }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="birthday" label="教师生日" width="180" align="center" />
        <el-table-column prop="education" label="教师学历" width="120" align="center">
          <template #default="scope">
            <el-tag :type="scope.row.education === 'Bachelor' 
              ? 'success' : scope.row.education === 'Master' 
              ? '' : 'warning'">
              {{
                scope.row.education === 'Bachelor' 
                ? '学士' : scope.row.education === 'Master' 
                ? '硕士' : '博士'
              }}
            </el-tag>
          </template>
        </el-table-column>

        <el-table-column prop="title" label="教师职称" width="120" align="center">
          <template #default="scope">
            <el-tag :type="
                      scope.row.title === 'Assistant' 
                      ? 'success' : scope.row.title === 'Lecturer' 
                      ? 'danger' : scope.row.title === 'Associate' 
                      ? '' : 'warning'
                    ">
              {{
                scope.row.title === 'Assistant' 
                ? '助教' : scope.row.title === 'Lecturer' 
                ? '讲师' : scope.row.title === 'Associate'
                ? '副教授': '教授'
              }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="department_name" label="院系名字" align="center">
        </el-table-column>

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
    <el-dialog :title="`${addOrUpdate ? '添加教师信息' : '编辑教师信息'}`" v-model="showDialog" width="30%">
      <el-form label-width="100px" ref="formRef" :model="formData" :rules="formRules"
        autocomplete="on">
        <el-form-item label="教师编号" prop="id">
          <el-input v-model="formData.id" placeholder="编号" :disabled=!addOrUpdate></el-input>
        </el-form-item>
        <el-form-item label="教师名字" prop="name">
          <el-input v-model="formData.name" placeholder="名字"></el-input>
        </el-form-item>

        <el-form-item label="教师性别" prop="sex">
          <el-select v-model="formData.sex" placeholder="请选择性别">
            <el-option key="1" label="男" value="man"></el-option>
            <el-option key="2" label="女" value="woman"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="教师生日">
          <el-form-item prop="birthday">
            <el-date-picker type="date" placeholder="请选择日期" v-model="formData.birthday"
              format="YYYY-MM-DD" value-format="YYYY-MM-DD" style="width: 100%;">
            </el-date-picker>
          </el-form-item>
        </el-form-item>

        <el-form-item label="教师密码" prop="password">
          <el-input v-model="formData.password" placeholder="请输入密码"></el-input>
        </el-form-item>

        <el-form-item label="教师学历" prop="education">
          <el-select v-model="formData.education" placeholder="请选择学历">
            <el-option key="1" label="学士" value="Bachelor"></el-option>
            <el-option key="2" label="硕士" value="Master"></el-option>
            <el-option key="3" label="博士" value="Doctor"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="教师职称" prop="title">
          <el-select v-model="formData.title" placeholder="请选择职称">
            <el-option key="1" label="助教" value="Assistant"></el-option>
            <el-option key="2" label="讲师" value="Lecturer"></el-option>
            <el-option key="3" label="副教授" value="Associate"></el-option>
            <el-option key="4" label="教授" value="Professor"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="院系名字" prop="department_id">
          <el-select v-model="formData.department_id" placeholder="请选择院系"
            @change="getChange(formData.department_id)">
            <el-option v-for="(dept, index) in deptData" :key=index :label=dept.name
              :value=dept.id />
          </el-select>
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
  read_teachers,
  create_teacher,
  update_teacher,
  delete_teacher,
} from '../../api/teacher';
import { read_departments } from '../../api/department';

// 定义icon和页面名字
const iconName = ref('cascades');
const pageName = ref('教师表');

const teacherData = ref([]); // 教师数据
const deptData = ref([]); // 院系数据
const pageTotal = ref(0); // 总个数

/**
 * getData()
 * 获取表格数据
 */
const getData = () => {
  read_teachers(query)
    .then((res) => {
      teacherData.value = res.data;
    })
    .catch(() => {
      ElMessage.error('加载教师信息数据失败！');
    });

  // 获取院系信息
  read_departments(query)
    .then((res) => {
      deptData.value = res.data;
    })
    .catch(() => {
      ElMessage.error('加载院系信息数据失败！');
    });
};

// 页面加载后调用函数
onMounted(() => {
  getData();
});

// 监听属性
watchEffect(() => {
  pageTotal.value = teacherData.value.length || 10;
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
      required: true,
      min: 6,
      max: 6,
      message: '教师编号的长度应为6',
      trigger: 'change',
    },
  ],
  name: [
    {
      required: 'true',
      message: '请输入教师名称',
      trigger: ['change', 'blur'],
    },
  ],
  sex: [
    {
      required: 'true',
      message: '请输入教师性别',
      trigger: 'change',
    },
  ],
  birthday: [
    {
      required: 'true',
      message: '请选择生日',
      trigger: 'change',
    },
  ],
  password: [
    {
      required: 'true',
      message: '请输入密码',
      trigger: ['change', 'blur'],
    },
  ],
  education: [
    {
      required: 'true',
      message: '请选择教师学历',
      trigger: 'change',
    },
  ],
  title: [
    {
      required: 'true',
      message: '请选择教师职称',
      trigger: 'change',
    },
  ],
  department_id: [
    {
      required: 'true',
      message: '请选择院系',
      trigger: ['change'],
    },
  ],
});

// 表单对象
const formData = reactive({
  id: '',
  name: '',
  sex: '',
  birthday: '',
  password: '',
  education: '',
  title: '',
  department_id: '',
});

let idx = -1; // 用户ID
let reIndex = -1; // 序号

/**
 * saveAdd
 * 确认添加
 */
const saveAdd = () => {
  showDialog.value = false;
  formRef.value.validate((valid) => {
    if (valid) {
      create_teacher(formData)
        .then((res) => {
          teacherData.value.push(res.data);
          ElMessage.success('成功添加教师信息！');
          getData();
        })
        .catch(() => {
          ElMessage.error('添加教师信息失败！');
        });
    } else {
      ElMessage.warning('教师信息填写有误，添加失败！');
    }
    // 重置表单
    formRef.value.resetFields();
  });
};

/**
 * handleEdit
 * 编辑用户信息
 */
const handleEdit = (index, row) => {
  idx = row.id;
  reIndex = index;
  Object.keys(formData).forEach((item) => {
    formData[item] = row[item];
  });

  getData();

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
      update_teacher(idx, formData)
        .then((res) => {
          ElMessage.success(`修改教师ID为 ${idx} 成功！`);
          Object.keys(res.data).forEach((item) => {
            teacherData.value[reIndex][item] = res.data[item];
          });
          getData();
        })
        .catch(() => {
          ElMessage.error('修改教师信息失败！');
        });
    } else {
      ElMessage.warning('填写教师信息有误，修改失败！');
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
      // 调用删除用户接口
      delete_teacher(idx)
        .then(() => {
          teacherData.value.splice(index, 1);
          ElMessage.success('删除成功！');
        })
        .catch(function (error) {
          ElMessage.success('删除成功！');
        });
    })
    .catch(() => {});
};

// 获取多选框的值
const getChange = (value) => {
  console.log(value);
};
</script>

<style scoped>
/* 选择框长度 */
.el-form-item .el-select {
  width: 100%;
}

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