<template>
  <div>
    <header-name :iconName='state.iconName' :pageName='state.pageName' />

    <!-- 表格 -->
    <div class="container">
      <!-- 排序和添加 -->
      <header-handle :query="query" :data="state.selectCourseData" :formData="formData"
        :isShowSearched="state.isShowSearched" :selectedList="state.selectedList"
        :read_datas="read_select_courses" :delete_data="delete_select_course"
        :removeSearch="removeSearch" @searchedData='searchedData' @isAddDialog='isAddDialog' />

      <!-- 表格信息 -->
      <el-table
        :data="state.isShowSearched 
                ? state.searched 
                : state.selectCourseData.slice((query.currentPage-1)*(query.pageSize),(query.currentPage)*(query.pageSize))"
        border stripe class="table" max-height="578"
        :default-sort="{ prop: 'id', order: 'ascending' }"
        @selection-change="handleSelectionChange">

        <!-- 勾选框 -->
        <el-table-column type="selection" width="80" align="center" />

        <!-- 序号 -->
        <el-table-column label="序号" type="index" width="80" align="center" fixed />

        <el-table-column prop="id" label="编号" width="140" align="center" sortable
          :sort-orders="['ascending', 'descending']" />
        <el-table-column prop="grade" label="成绩" width="140" align="center" />
        <el-table-column prop="student_name" width="140" label="学生姓名" align="center" />
        <el-table-column prop="teacher_name" width="140" label="教师姓名" align="center" />
        <el-table-column prop="course_name" min-width="220" label="课程名" align="center" />

        <!-- 操作 -->
        <handle :data="state.selectCourseData" :formData="formData"
          :delete_data="delete_select_course" :removeSearch="removeSearch"
          @isAddDialog='isAddDialog' @subIndexId='subIndexId' />
      </el-table>

      <!-- 页码 -->
      <pagination :pageSize="query.pageSize" :pageTotal="state.pageTotal"
        :currentPage="query.currentPage" :render='getData' @pageIndex='pageIndex' />
    </div>

    <!-- 编辑弹出框 -->
    <el-dialog :title="`${state.addOrUpdate ? '添加选课信息' : '编辑选课信息'}`" v-model="state.showDialog"
      width="30%">

      <el-form status-icon label-width="100px" ref="formRef" :model="formData" :rules="formRules"
        autocomplete="on">
        <el-form-item label="编号" prop="id" v-show="!state.addOrUpdate">
          <el-input v-model="formData.id" placeholder="编号" :disabled=!state.addOrUpdate />
        </el-form-item>
        <el-form-item label="成绩" prop="grade">
          <el-input v-model="formData.grade" placeholder="成绩" maxlength="3" />
        </el-form-item>

        <el-form-item label="学生" prop="student_id">
          <el-select v-model="formData.student_id" placeholder="学生名"
            @change="getChange(formData.student_id)">
            <el-option v-for="(student, index) in state.studentData" :key=index :label=student.name
              :value=student.id />
          </el-select>
        </el-form-item>

        <el-form-item label="教师" prop="teacher_id">
          <el-select v-model="formData.teacher_id" placeholder="教师名"
            @change="getChange(formData.teacher_id)">
            <el-option v-for="(teacher, index) in state.teacherData" :key=index :label=teacher.name
              :value=teacher.id />
          </el-select>
        </el-form-item>

        <el-form-item label="课程" prop="course_id">
          <el-select v-model="formData.course_id" placeholder="课程名"
            @change="getChange(formData.course_id)">
            <el-option v-for="(course, index) in state.courseData" :key=index :label=course.name
              :value=course.id />
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
  read_select_courses,
  create_select_course,
  update_select_course,
  delete_select_course,
} from '../../api/selectCourse';
import { read_students } from '../../api/student';
import { read_teachers } from '../../api/teacher';
import { read_courses } from '../../api/course';

// 变量
const state = reactive({
  iconName: 'cascades', // 页面icon名字
  pageName: '选课表', // 页面名字
  majorData: [], // 专业表数据
  selectCourseData: [], // 选课表数据
  studentData: [], // 学生表数据
  teacherData: [], // 教师表数据
  courseData: [], // 课程表数据
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
  read_select_courses()
    .then((res) => {
      state.selectCourseData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载选课信息数据失败！');
    });

  // 获取学生信息
  read_students()
    .then((res) => {
      state.studentData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载学生信息数据失败！');
    });

  // 获取学生信息
  read_teachers()
    .then((res) => {
      state.teacherData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载教师信息数据失败！');
    });

  // 获取学生信息
  read_courses()
    .then((res) => {
      state.courseData = res.data;
    })
    .catch(() => {
      ElMessage.error('加载课程信息数据失败！');
    });
}

// 页面加载后调用函数
onMounted(() => {
  getData();
});

// 监听属性
watchEffect(() => {
  state.pageTotal = state.selectCourseData.length || query.pageSize;
});

// 当前页码
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
  grade: '',
  student_id: '',
  teacher_id: '',
  course_id: '',
});

// 定义校验规则
const formRules = reactive({
  grade: [{ message: '请输入成绩(默认为0)', trigger: ['change', 'blur'] }],
  student_id: [{ required: 'true', message: '请选课学生', trigger: 'change' }],
  teacher_id: [{ required: 'true', message: '请选择教师', trigger: 'change' }],
  course_id: [
    { required: 'true', message: '请选课课程', trigger: ['change', 'blur'] },
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
 * saveAdd
 * 确认添加
 */
function saveAdd() {
  state.showDialog = false;

  formRef.value.validate((valid) => {
    if (valid) {
      create_select_course(formData)
        .then((res) => {
          state.selectCourseData.push(res.data);
          ElMessage.success(`成功添加编号为${res.data.id}的选课信息！`);
          removeSearch();
        })
        .catch(() => {
          ElMessage.error('添加选课信息失败！');
        });
    } else {
      ElMessage.warning('选课信息不符合校验规则，添加失败！');
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
      update_select_course(idx, formData)
        .then((res) => {
          ElMessage.success(`修改选课ID为 ${idx} 成功！`);
          Object.keys(res.data).forEach((item) => {
            state.selectCourseData[reIndex][item] = res.data[item];
          });
          state.searched[0] = formData;
          getData();
        })
        .catch(() => {
          ElMessage.error('修改选课信息失败！');
        });
    } else {
      ElMessage.warning('填写选课不符合校验规则，修改失败！');
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