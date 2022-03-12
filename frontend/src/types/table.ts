/**
 * 路径参数类型(限定可选值)
 */
export enum pathEnum {
  dept = "department",
  major = "major",
  teacher = "teacher",
  student = "student",
  course = "course",
  elective = "selectCourse",
}

/**
 * 查询参数类型
 */
export interface queryType {
  id: string; // 请求id
  currentPage: number; // 页码
  pageSize: number; // 每页个数
}

/**
 * form表单时间数据类型(创建时间和更新时间)
 */
export interface formTimeType {
  gmt_create?: string; // 创建时间
  gmt_modify?: string; // 更新时间
}

/**
 * 院系表数据类型(请使用 ?: , 后面继承接口用到)
 */
export interface deptFormType extends formTimeType {
  id: number | string; // 编号
  name?: string; // 名称
  chairman?: string; // 主任名
  phone?: string; // 手机号
}

/**
 * 专业表数据类型
 */
export interface majorFormType extends formTimeType {
  id: number | string; // 编号
  name?: string; // 名称
  assistant?: string; // 辅导员名
  phone?: string; // 手机号
  department_id?: number | string; // 院系编号
}

/**
 * 教师表数据类型
 */
export interface teachFormType extends formTimeType {
  id: number | string; // 编号
  name?: string; // 名称
  sex?: "0" | "1"; // 性别
  birthday?: string; // 生日
  education?: "1" | "2" | "3"; // 学历
  title?: "1" | "2" | "3" | "4"; // 职称
  address?: string; // 地址
  image?: string; //头像
  password?: string; // 密码
  department_id?: number | string; // 院系编号
}

/**
 * 学生表数据类型
 */
export interface stuFormType extends formTimeType {
  id: number | string; // 编号
  name?: string; // 名称
  sex?: "0" | "1"; // 性别
  birthday?: string; // 生日
  address?: string; // 地址
  image?: string; //头像
  password?: string; // 密码
  major_id?: number | string; // 专业编号
}

/**
 * 课程表数据类型
 */
export interface courseFormType extends formTimeType {
  id: number | string; // 编号
  name?: string; // 名称
  credit?: number | string; // 学分
  period?: number | string; // 学时
}

/**
 * 选课表数据类型
 */
export interface selectCourseFormType extends formTimeType {
  id: number | string; // 编号
  grade?: number | string; // 成绩
  student_id?: number | string; // 学生编号
  teacher_id?: number | string; // 教师编号
  course_id?: number | string; // 课程编号
}

/**
 * form表单数据类型
 */
export interface formDataType
  extends deptFormType,
    majorFormType,
    teachFormType,
    stuFormType,
    courseFormType,
    selectCourseFormType {}

/**
 * 依赖数据类型
 */
export interface relationData {
  id: string | number; // 编号
  name: string; // 名称
}
