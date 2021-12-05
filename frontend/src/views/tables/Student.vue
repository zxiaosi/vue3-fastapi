<template>
  <div>
    <header-name :iconName='state.iconName' :pageName='state.pageName' />

    <!-- 表格 -->
    <div class="container">
      <!-- 排序和添加 -->
      <header-handle :query="query" :data="state.studentData" :formData="formData"
        :isShowSearched="state.isShowSearched" :selectedList="state.selectedList"
        :read_datas="read_students" :delete_data="delete_student" :removeSearch="removeSearch"
        @searchedData='searchedData' @isAddDialog='isAddDialog' />

      <!-- 表格信息 -->
      <el-table
        :data="state.isShowSearched 
                ? state.searched 
                : state.studentData.slice((query.currentPage-1)*(query.pageSize),(query.currentPage)*(query.pageSize))"
        border stripe class="table" max-height="578"
        :default-sort="{ prop: 'id', order: 'ascending' }"
        @selection-change="handleSelectionChange">

        <!-- 勾选框 -->
        <el-table-column type="selection" width="80" align="center" />

        <!-- 序号 -->
        <el-table-column label="序号" type="index" width="80" align="center" fixed />

        <el-table-column prop="id" label="学号" width="140" align="center" sortable
          :sort-orders="['ascending', 'descending']" />
        <el-table-column prop="name" label="学生名字" width="140" align="center" />
        <el-table-column prop="sex" label="学生性别" width="140" align="center">
          <template #default="scope">
            <el-tag :type="scope.row.sex === 'man' ? 'success': 'danger'">
              {{ scope.row.sex=== 'man' ? '男': '女' }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="birthday" label="学生生日" width="220" align="center" sortable
          :sort-orders="['ascending', 'descending']" />
        <el-table-column prop="major_name" label="专业名字" min-width="220" align="center" />

        <!-- 操作 -->
        <handle :data="state.studentData" :formData="formData" :delete_data="delete_student"
          :removeSearch="removeSearch" @isAddDialog='isAddDialog' @subIndexId='subIndexId' />
      </el-table>

      <!-- 页码 -->
      <pagination :pageSize="query.pageSize" :pageTotal="state.pageTotal"
        :currentPage="query.currentPage" :render='getData' @pageIndex='pageIndex' />
    </div>

    <!-- 编辑弹出框 -->
    <el-dialog :title="`${state.addOrUpdate ? '添加学生信息' : '编辑学生信息'}`" v-model="state.showDialog"
      width="30%">

      <el-form status-icon label-width="100px" ref="formRef" :model="formData" :rules="formRules"
        autocomplete="on">
        <el-form-item label="学生编号" prop="id">
          <el-input v-model="formData.id" placeholder="编号" maxlength="10"
            :disabled=!state.addOrUpdate />
        </el-form-item>
        <el-form-item label="学生名字" prop="name">
          <el-input v-model="formData.name" placeholder="名字" maxlength="10" />
        </el-form-item>

        <el-form-item label="学生性别" prop="sex">
          <el-select v-model="formData.sex" placeholder="请选择性别">
            <el-option key="1" label="男" value="man" />
            <el-option key="2" label="女" value="woman" />
          </el-select>
        </el-form-item>

        <el-form-item label="学生生日">
          <el-form-item prop="birthday">
            <el-date-picker type="date" placeholder="请选择日期" v-model="formData.birthday"
              format="YYYY-MM-DD" value-format="YYYY-MM-DD" style="width: 100%;">
            </el-date-picker>
          </el-form-item>
        </el-form-item>

        <el-form-item label="学生密码" prop="password">
          <el-input v-model="formData.password" placeholder="请输入密码" maxlength="20" />
        </el-form-item>

        <el-form-item label="专业名字" prop="major_id">
          <el-select v-model="formData.major_id" placeholder="请选择专业"
            @change="getChange(formData.major_id)">
            <el-option v-for="(major, index) in state.majorData" :key=index :label=major.name
              :value=major.id />
          </el-select>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="state.showDialog = false">取 消</el-button>
          <el-button type="primary" v-if="state.addOrUpdate" @click="saveAdd">添 加</el-button>
          <el-button type="primary" v-else @click="saveEdit">更 新</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, watchEffect } from 'vue';
import { ElMessage } from 'element-plus';
import HeaderName from '../../components/tables/HeaderName.vue';
import HeaderHandle from '../../components/tables/HeaderHandle.vue';
import Handle from '../../components/tables/Handle.vue';
import Pagination from '../../components/tables/Pagination.vue';
import {
  read_students,
  create_student,
  update_student,
  delete_student,
} from '../../api/student';
import { read_majors } from '../../api/major';

// 变量
const state = reactive({
  iconName: 'cascades', // 页面icon名字
  pageName: '学生表', // 页面名字
  studentData: [], // 学生表数据
  majorData: [], // 专业表数据
  pageTotal: 0, // 总个数
  isShowSearched: false, // 是否显示被搜索的
  searched: [], // 被搜索的数据(渲染表格数据需要是列表)
  selectedList: [], // 被勾选的的值
  showDialog: false, // 是否显示弹窗
  addOrUpdate: true, // 是否是添加或更新(true-添加 | false-更新)
});

// 搜索和页码
const query = reactive({
  id: '',
  currentPage: 1,
  pageSize: 10,
});

let idx = -1; // 临时编号
let reIndex = -1; // 临时序号

/**
 * 获取表格数据
 */
function getData() {
  read_students()
    .then((res) => {
      state.studentData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载学生信息数据失败！');
    });

  // 获取专业信息
  read_majors()
    .then((res) => {
      state.majorData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载专业信息数据失败！');
    });
}

// 页面加载后调用函数
onMounted(() => {
  getData();
});

// 监听属性
watchEffect(() => {
  state.pageTotal = state.studentData.length || query.pageSize;
});

/**
 * 当前页码(子组件传递的值)
 */
function pageIndex(res) {
  query.currentPage = res;
}

/**
 * 显示被搜索的数据(子组件传值)
 */
function searchedData(res) {
  state.isShowSearched = true;
  state.searched.splice(0, 1, res);
}

/**
 * 被勾选的数据
 */
function handleSelectionChange(val) {
  if (val.length == 0) {
    state.selectedList = [];
  }

  val.forEach((item, index) => {
    state.selectedList.splice(index, 1, { reIndex: index, idx: item.id });
  });
}

// 校验规则
const formRef = ref();

// 表单对象
const formData = reactive({
  id: '',
  name: '',
  sex: '',
  birthday: '',
  password: '',
  major_id: '',
});

// 定义校验规则
const formRules = reactive({
  id: [
    {
      required: true,
      min: 10,
      message: '学生编号的长度应为10',
      trigger: 'change',
    },
  ],
  name: [
    {
      required: 'true',
      message: '请输入学生名称',
      trigger: ['change', 'blur'],
    },
  ],
  sex: [{ required: 'true', message: '请输入学生性别', trigger: 'change' }],
  birthday: [{ required: 'true', message: '请选择生日', trigger: 'change' }],
  password: [
    { required: 'true', message: '请输入密码', trigger: ['change', 'blur'] },
  ],
  major_id: [{ required: 'true', message: '请选择专业', trigger: ['change'] }],
});

/**
 * 添加、编辑表格的弹窗(子组件传递的值)
 */
function isAddDialog(show, addUpdate) {
  state.showDialog = show;
  state.addOrUpdate = addUpdate;
}

/**
 * 确认添加
 */
function saveAdd() {
  state.showDialog = false;

  formRef.value.validate((valid) => {
    if (valid) {
      create_student(formData)
        .then((res) => {
          if (res.code == 200) {
            state.studentData.push(res.data);
            ElMessage.success(`成功添加编号为${res.data.id}的学生信息！`);
            removeSearch();
          } else {
            ElMessage.warning('教师表信息填写有误，添加失败！');
          }
        })
        .catch(() => {
          ElMessage.error('添加学生信息失败！');
        });
    } else {
      ElMessage.warning('学生信息不符合校验规则，添加失败！');
    }
    // 重置表单
    formRef.value.resetFields();
  });
}

/**
 * 获取索引和编号
 */
function subIndexId(index, id) {
  reIndex = index;
  idx = id;
}

/**
 * 确认更新
 */
function saveEdit() {
  state.showDialog = state.addOrUpdate = false;

  formRef.value.validate((valid) => {
    if (valid) {
      update_student(idx, formData)
        .then((res) => {
          ElMessage.success(`修改学生ID为 ${idx} 成功！`);
          Object.keys(res.data).forEach((item) => {
            state.studentData[reIndex][item] = res.data[item];
          });
          state.searched[0] = formData;
          getData();
        })
        .catch(() => {
          ElMessage.error('修改学生信息失败！');
        });
    } else {
      ElMessage.warning('填写学生信息有误，修改失败！');
    }
  });
}

/**
 * 获取多选框的值
 */
function getChange(value) {
  console.log(value);
}

/**
 * 清除搜索
 */
function removeSearch() {
  query.id = '';
  state.isShowSearched = false;
  getData();
}
</script>

<style scoped>
/* 选择框长度 */
.el-form-item .el-select {
  width: 100%;
}
.table {
  width: 100%;
  font-size: 14px;
}
.table-td-thumb {
  display: block;
  margin: auto;
  width: 40px;
  height: 40px;
}
</style>