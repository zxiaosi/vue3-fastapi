/**
 * 路径参数类型(限定可选值)
 */
export enum PathEnum {
  dept = "department",
  major = "major",
  teacher = "teacher",
  student = "student",
  course = "course",
  taught = "taught",
  elective = "elective",
}

/**
 * 查询参数类型
 */
export interface Query {
  id: string; // 请求id
  currentPage: number; // 页码
  pageSize: number; // 每页个数
}

/**
 * form表单时间数据类型(创建时间和更新时间)
 */
export interface TimeForm {
  create_time?: string; // 创建时间
  update_time?: string; // 更新时间
}

/**
 * 院系表数据类型(请使用 ?: , 后面继承接口用到)
 */
export interface DeptForm extends TimeForm {
  id?: number | string; // 编号
  name?: string; // 名称
  chairman?: string; // 主任名
  phone?: string; // 手机号
}

/**
 * 专业表数据类型
 */
export interface MajorForm extends TimeForm {
  id?: number | string; // 编号
  name?: string; // 名称
  assistant?: string; // 辅导员名
  phone?: string; // 手机号
  departmentId?: number | string; // 院系编号
}

/**
 * 教师表数据类型
 */
export interface TeacherForm extends TimeForm {
  id?: number | string; // 编号
  name?: string; // 名称
  sex?: "0" | "1"; // 性别
  birthday?: string; // 生日
  education?: "1" | "2" | "3"; // 学历
  title?: "1" | "2" | "3" | "4"; // 职称
  address?: string; // 地址
  image?: string; //头像
  password?: string; // 密码
  departmentId?: number | string; // 院系编号
}

/**
 * 学生表数据类型
 */
export interface StudentForm extends TimeForm {
  id?: number | string; // 编号
  name?: string; // 名称
  sex?: "0" | "1"; // 性别
  birthday?: string; // 生日
  address?: string; // 地址
  image?: string; //头像
  password?: string; // 密码
  majorId?: number | string; // 专业编号
}

/**
 * 课程表数据类型
 */
export interface CourseForm extends TimeForm {
  id?: number | string; // 编号
  name?: string; // 名称
  credit?: number | string; // 学分
  period?: number | string; // 学时
}

/**
 * 讲授表数据类型
 */
export interface TaughtForm extends TimeForm {
  id?: number | string; // 编号
  grade?: number | string; // 成绩
  teacherId?: number | string; // 教师编号
  courseId?: number | string; // 课程编号
}

/**
 * 选课表数据类型
 */
export interface ElectiveForm extends TimeForm {
  id?: number | string; // 编号
  grade?: number | string; // 成绩
  studentId?: number | string; // 学生编号
  courseId?: number | string; // 课程编号
}

/**
 * form表单数据类型
 */
export interface FormData extends DeptForm, MajorForm, TeacherForm, StudentForm, CourseForm, TaughtForm, ElectiveForm {}
