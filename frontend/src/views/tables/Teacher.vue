<template>
  <div>
    <header-name :iconName='state.iconName' :pageName='state.pageName' />

    <!-- 表格 -->
    <div class="container">
      <!-- 排序和添加 -->
      <header-handle :query="query" :data="state.teacherData" :formData="formData"
        :isShowSearched="state.isShowSearched" :selectedList="state.selectedList"
        :read_datas="read_teachers" :delete_data="delete_teacher" :removeSearch="removeSearch"
        @searchedData='searchedData' @isAddDialog='isAddDialog' />

      <!-- 表格信息 -->
      <el-table
        :data="state.isShowSearched 
                ? state.searched 
                : state.teacherData.slice((query.currentPage-1)*(query.pageSize),(query.currentPage)*(query.pageSize))"
        border stripe class="table" max-height="578"
        :default-sort="{ prop: 'id', order: 'ascending' }"
        @selection-change="handleSelectionChange">

        <!-- 勾选框 -->
        <el-table-column type="selection" width="80" align="center" />

        <!-- 序号 -->
        <el-table-column label="序号" type="index" width="80" align="center" fixed />

        <el-table-column prop="id" label="职工号" width="140" align="center" sortable
          :sort-orders="['ascending', 'descending']" />
        <el-table-column prop="name" label="教师名字" width="140" align="center" />

        <el-table-column prop="sex" label="教师性别" width="140" align="center">
          <template #default="scope">
            <el-tag :type="scope.row.sex === 'man' ? 'success': 'danger'">
              {{ scope.row.sex=== 'man' ? '男': '女' }}
            </el-tag>
          </template>
        </el-table-column>

        <el-table-column prop="birthday" label="教师生日" width="220" align="center" sortable
          :sort-orders="['ascending', 'descending']" />

        <el-table-column prop="education" label="教师学历" width="140" align="center">
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

        <el-table-column prop="title" label="教师职称" width="140" align="center">
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

        <el-table-column prop="department_name" label="院系名字" min-width="220" align="center" />

        <!-- 操作 -->
        <handle :data="state.teacherData" :formData="formData" :delete_data="delete_teacher"
          :removeSearch="removeSearch" @isAddDialog='isAddDialog' @subIndexId='subIndexId' />
      </el-table>

      <!-- 页码 -->
      <pagination :pageSize="query.pageSize" :pageTotal="state.pageTotal"
        :currentPage="query.currentPage" :render='getData' @pageIndex='pageIndex' />
    </div>

    <!-- 编辑弹出框 -->
    <el-dialog :title="`${state.addOrUpdate ? '添加教师信息' : '编辑教师信息'}`" v-model="state.showDialog"
      width="30%">

      <el-form status-icon label-width="100px" ref="formRef" :model="formData" :rules="formRules"
        autocomplete="on">
        <el-form-item label="教师编号" prop="id">
          <el-input v-model="formData.id" placeholder="编号" maxlength="6"
            :disabled=!state.addOrUpdate />
        </el-form-item>
        <el-form-item label="教师名字" prop="name">
          <el-input v-model="formData.name" placeholder="名字" maxlength="10" />
        </el-form-item>

        <el-form-item label="教师性别" prop="sex">
          <el-select v-model="formData.sex" placeholder="请选择性别">
            <el-option key="1" label="男" value="man" />
            <el-option key="2" label="女" value="woman" />
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
          <el-input v-model="formData.password" placeholder="请输入密码" maxlength="20" />
        </el-form-item>

        <el-form-item label="教师学历" prop="education">
          <el-select v-model="formData.education" placeholder="请选择学历">
            <el-option key="1" label="学士" value="Bachelor" />
            <el-option key="2" label="硕士" value="Master" />
            <el-option key="3" label="博士" value="Doctor" />
          </el-select>
        </el-form-item>

        <el-form-item label="教师职称" prop="title">
          <el-select v-model="formData.title" placeholder="请选择职称">
            <el-option key="1" label="助教" value="Assistant" />
            <el-option key="2" label="讲师" value="Lecturer" />
            <el-option key="3" label="副教授" value="Associate" />
            <el-option key="4" label="教授" value="Professor" />
          </el-select>
        </el-form-item>

        <el-form-item label="院系名字" prop="department_id">
          <el-select v-model="formData.department_id" placeholder="请选择院系"
            @change="getChange(formData.department_id)">
            <el-option v-for="(dept, index) in state.deptData" :key=index :label=dept.name
              :value=dept.id />
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
  read_teachers,
  create_teacher,
  update_teacher,
  delete_teacher,
} from '../../api/teacher';
import { read_departments } from '../../api/department';

// 变量
const state = reactive({
  iconName: 'cascades', // 页面icon名字
  pageName: '教师表', // 页面名字
  teacherData: [], // 教师表数据
  deptData: [], // 院系表数据
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
  read_teachers()
    .then((res) => {
      state.teacherData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载教师信息数据失败！');
    });

  // 获取院系信息
  read_departments()
    .then((res) => {
      state.deptData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载院系信息数据失败！');
    });
}

// 页面加载后调用函数
onMounted(() => {
  getData();
});

// 监听属性
watchEffect(() => {
  state.pageTotal = state.teacherData.length || query.pageSize;
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
  education: '',
  title: '',
  department_id: '',
});

// 定义校验规则
const formRules = reactive({
  id: [
    {
      required: true,
      min: 6,
      message: '教师编号的长度应为6',
      trigger: 'change',
    },
  ],
  name: [
    {
      required: 'true',
      message: '请输入教师名称(最大长度为10)',
      trigger: ['change', 'blur'],
    },
  ],
  sex: [{ required: 'true', message: '请输入教师性别', trigger: 'change' }],
  birthday: [{ required: 'true', message: '请选择生日', trigger: 'change' }],
  password: [
    { required: 'true', message: '请输入密码', trigger: ['change', 'blur'] },
  ],
  education: [
    { required: 'true', message: '请选择教师学历', trigger: 'change' },
  ],
  title: [{ required: 'true', message: '请选择教师职称', trigger: 'change' }],
  department_id: [
    { required: 'true', message: '请选择院系', trigger: ['change'] },
  ],
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
      create_teacher(formData)
        .then((res) => {
          if (res.code == 200) {
            state.teacherData.push(res.data);
            ElMessage.success(`成功添加编号为${res.data.id}的教师信息！`);
            removeSearch();
          } else {
            ElMessage.warning('院系信息填写有误，添加失败！');
          }
        })
        .catch(() => {
          ElMessage.error('添加教师信息失败！');
        });
    } else {
      ElMessage.warning('教师信息不符合校验规则，添加失败！');
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
  state.addOrUpdate = state.showDialog = false;

  formRef.value.validate((valid) => {
    if (valid) {
      update_teacher(idx, formData)
        .then((res) => {
          ElMessage.success(`修改教师ID为 ${idx} 成功！`);
          Object.keys(res.data).forEach((item) => {
            state.teacherData[reIndex][item] = res.data[item];
          });
          state.searched[0] = formData;
          getData();
        })
        .catch(() => {
          ElMessage.error('修改教师信息失败！');
        });
    } else {
      ElMessage.warning('填写教师信息不符合校验规则，修改失败！');
    }
  });
}

/*
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
/* 选中框长度 */
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