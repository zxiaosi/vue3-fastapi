#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : zxiaosi
# @desc : 选课表的Pydantic数据验证
from pydantic import BaseModel, Field


# id 使用 str 为了能够使用正则表达式匹配
# ... 表示必填, 和max_length冲突, 使用max_length可以输入空值
# Optional[str]: union[str, None] --> 表示 数据可以为str类型或者为空

# 共享JSON字段
class SelectCourseIn(BaseModel):
    grade: str = Field(default=0, regex=r'^100|(^([0]{0})([1-9]{0,1})([0-9]{1}))$', max_length=3, example='成绩',
                       title='成绩')
    student_id: str = Field(regex=r'^[1-9][0-9]{9}$', min_length=10, max_length=10, example='学号：1810020401', title='学号')
    teacher_id: str = Field(regex=r'^[1-9][0-9]{5}$', min_length=6, max_length=6, example='职工号：180404', title='职工号')
    course_id: str = Field(regex=r'^[1-9][0-9]{3}$', min_length=4, max_length=4, example='课程编号：1101', title='课程编号')


# 添加数据的JSON字段
class SelectCourseCreate(SelectCourseIn):
    pass


# 更新数据的JSON字段
class SelectCourseUpdate(SelectCourseIn):
    pass


# 查询数据的JSON字段
class SelectCourseOut(SelectCourseIn):
    id: int = Field(..., example='自增编号', title='编号')

    class Config:
        orm_mode = True  # 是否使用orm模型
