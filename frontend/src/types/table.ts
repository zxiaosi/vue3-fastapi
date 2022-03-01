/**
 * 路径参数
 */
export interface pathType {
  path: "department" | "major" | "teacher" | "student" | "course" | "selectCourse"; // 限定可选值
}

/**
 * 表格页面信息
 */
export interface pageType {
  icon: string; // 阿里云图标 `el-icon-ali-${icon}`
  zhName: string; // 页面中文名
  enName: pathType["path"]; // 页面英文名
}

/**
 * 自定义枚举
 */
export interface enumType {
  [key: string]: { name: string; tag: string };
}

/**
 * 查询参数
 */
export interface queryType {
  id: string; // 请求id
  currentPage: number; // 页码
  pageSize: number; // 每页个数
}

/**
 * form表单数据
 */
export interface formDataType {
  id: number | string; // 编号
  name?: string; // 名字
  chairman?: string; // 主任名
  assistant?: string; // 辅导员名
  phone?: number | string; // 手机号
  sex?: "man" | "woman"; // 性别
  birthday?: string; // 生日
  password?: string; // 密码
  education?: "Bachelor" | "Master" | "Doctor"; // 学位
  title?: "Assistant" | "Lecturer" | "Associate" | "Professor"; // 职称
  credit?: number | string; // 学分
  period?: number | string; // 学时
  grade?: string; // 成绩
  department_id?: number | string; // 院系编号
  major_id?: number | string; // 专业编号
  student_id?: string; // 学生编号
  teacher_id?: string; // 教师编号
  course_id?: string; // 课程编号
  gmt_create?: string; // 创建时间
  gmt_modify?: string; // 更新时间
}

/**
 * 依赖数据
 */
export interface relationData {
  id: string | number; // 编号
  name: string; // 名称
}
