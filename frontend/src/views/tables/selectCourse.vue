<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-ali-cascades"></i> 选课表
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
        :data="selectCourseData.slice((query.pageIndex-1)*(query.pageSize),(query.pageIndex)*(query.pageSize))"
        border class="table" ref="multipleTable" header-cell-class-name="table-header">

        <!-- 序号 -->
        <el-table-column type="index" width="80" label="序号" align="center">
          <template #default="scope">
            <span>{{scope.$index+((query.pageIndex) - 1) * (query.pageSize) + 1}} </span>
          </template>
        </el-table-column>

        <el-table-column prop="id" label="编号" align="center" />
        <el-table-column prop="grade" label="成绩" align="center" />
        <el-table-column prop="student_name" label="学号" align="center" />
        <el-table-column prop="teacher_name" label="职工号" align="center" />
        <el-table-column prop="course_name" label="课程编号" align="center">
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
    <el-dialog :title="`${addOrUpdate ? '添加选课信息' : '编辑选课信息'}`" v-model="showDialog" width="30%">
      <el-form label-width="100px" ref="formRef" :model="formData" :rules="formRules"
        autocomplete="on">
        <el-form-item label="编号" prop="id" v-show="!addOrUpdate">
          <el-input v-model="formData.id" placeholder="编号" :disabled=!addOrUpdate />
        </el-form-item>
        <el-form-item label="成绩" prop="grade">
          <el-input v-model="formData.grade" placeholder="名字" />
        </el-form-item>

        <el-form-item label="学号" prop="student_id">
          <el-select v-model="formData.student_id" placeholder="请选择学号"
            @change="getChange(formData.student_id)">
            <el-option v-for="(student, index) in studentData" :key=index :label=student.name
              :value=student.id />
          </el-select>
        </el-form-item>

        <el-form-item label="职工号" prop="teacher_id">
          <el-select v-model="formData.teacher_id" placeholder="请选择职工号"
            @change="getChange(formData.teacher_id)">
            <el-option v-for="(teacher, index) in teacherData" :key=index :label=teacher.name
              :value=teacher.id />
          </el-select>
        </el-form-item>

        <el-form-item label="课程编号" prop="course_id">
          <el-select v-model="formData.course_id" placeholder="请选择课程编号"
            @change="getChange(formData.course_id)">
            <el-option v-for="(course, index) in courseData" :key=index :label=course.name
              :value=course.id />
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

<script>
import { ref, reactive, onMounted, watchEffect } from 'vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import {
  read_select_courses,
  create_select_course,
  update_select_course,
  delete_select_course,
} from '../../api/selectCourse';
import { read_students } from '../../api/student';
import { read_teachers } from '../../api/teacher';
import { read_courses } from '../../api/course';

export default {
  name: 'selectCourse',
  setup() {
    const selectCourseData = ref([]); // 选课数据
    const studentData = ref([]); // 学生数据
    const teacherData = ref([]); // 教师数据
    const courseData = ref([]); // 课程数据
    const pageTotal = ref(0); // 总个数

    /**
     * getData()
     * 获取表格数据
     */
    const getData = () => {
      read_select_courses(query)
        .then((res) => {
          selectCourseData.value = res.data;
        })
        .catch(() => {
          ElMessage.error('加载选课信息数据失败！');
        });

      // 获取学生信息
      read_students(query)
        .then((res) => {
          studentData.value = res.data;
        })
        .catch(() => {
          ElMessage.error('加载学生信息数据失败！');
        });

      // 获取学生信息
      read_teachers(query)
        .then((res) => {
          teacherData.value = res.data;
        })
        .catch(() => {
          ElMessage.error('加载教师信息数据失败！');
        });

      // 获取学生信息
      read_courses(query)
        .then((res) => {
          courseData.value = res.data;
        })
        .catch(() => {
          ElMessage.error('加载课程信息数据失败！');
        });
    };

    // 页面加载后调用函数
    onMounted(() => {
      getData();
    });

    // 监听属性
    watchEffect(() => {
      pageTotal.value = selectCourseData.value.length || 10;
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
        selectCourseData.value.sort((a, b) => a.id - b.id);
      } else {
        selectCourseData.value.sort((a, b) => b.id - a.id);
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
      grade: [
        {
          message: '请输入成绩(默认为0)',
          trigger: ['change', 'blur'],
        },
      ],
      student_id: [
        {
          required: 'true',
          message: '请选课学生',
          trigger: 'change',
        },
      ],
      teacher_id: [
        {
          required: 'true',
          message: '请选择教师',
          trigger: 'change',
        },
      ],
      course_id: [
        {
          required: 'true',
          message: '请选课课程',
          trigger: ['change', 'blur'],
        },
      ],
    });

    // 表单对象
    const formData = reactive({
      id: '',
      name: '',
      sex: '',
      student_id: '',
      teacher_id: '',
      course_id: '',
    });

    let idx = -1; // 用户ID
    let reIndex = -1; // 序号

    /**
     * handleAdd
     * 添加用户信息
     */
    const handleAdd = (event) => {
      clickRecover(event);

      // 重置表单(防止编辑页面数据)
      Object.keys(formData).forEach((key) => (formData[key] = ''));

      getData();

      // 显示弹窗(添加)
      addOrUpdate.value = true;
      showDialog.value = true;
    };

    /**
     * saveAdd
     * 确认添加
     */
    const saveAdd = () => {
      showDialog.value = false;
      formRef.value.validate((valid) => {
        if (valid) {
          create_select_course(formData)
            .then((res) => {
              selectCourseData.value.push(res.data);
              ElMessage.success('成功添加选课信息！');
              getData();
            })
            .catch(() => {
              ElMessage.error('添加选课信息失败！');
            });
        } else {
          ElMessage.warning('选课信息填写有误，添加失败！');
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
          update_select_course(idx, formData)
            .then((res) => {
              ElMessage.success(`修改选课ID为 ${idx} 成功！`);
              Object.keys(res.data).forEach((item) => {
                selectCourseData.value[reIndex][item] = res.data[item];
              });
              getData();
            })
            .catch(() => {
              ElMessage.error('修改选课信息失败！');
            });
        } else {
          ElMessage.warning('填写选课信息有误，修改失败！');
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
          delete_select_course(idx)
            .then(() => {
              selectCourseData.value.splice(index, 1);
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

    // 获取多选框的值
    const getChange = (value) => {
      console.log(value);
    };

    // 返回
    return {
      query,
      selectCourseData,
      studentData,
      teacherData,
      courseData,
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
      saveAdd,
      handleEdit,
      saveEdit,
      handleDelete,
      getChange,
    };
  },
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