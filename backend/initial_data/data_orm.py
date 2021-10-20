#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 20:48
# @Author : 小四先生
# @desc : data_core中数据的加工(被 sqlalchemy_orm_initial函数 使用)

# * 表示 [userData, departmentData, majorData, studentData, teacherData, adminData, courseData, selectCourseData]
from .data_core import *
# * 表示 [User, Department, Major, Student, Teacher, Admin, Course, SelectCourse]
from backend.models import *

data = []

for user in userData:
    data.append(User(full_name=user['full_name'], hashed_password=user['hashed_password']))

for department in departmentData:
    data.append(
        Department(
            id=department['id'],
            name=department['name'],
            chairman=department['chairman'],
            phone=department['phone']
        )
    )

for major in majorData:
    data.append(
        Major(
            id=major['id'],
            name=major['name'],
            assistant=major['assistant'],
            phone=major['phone'],
            department_id=major['department_id']
        )
    )

for student in studentData:
    data.append(
        Student(
            id=student['id'],
            name=student['name'],
            sex=student['sex'],
            birthday=student['birthday'],
            hashed_password=student['hashed_password'],
            major_id=student['major_id'],
        )
    )

for teacher in teacherData:
    data.append(
        Teacher(
            id=teacher['id'],
            name=teacher['name'],
            sex=teacher['sex'],
            birthday=teacher['birthday'],
            hashed_password=teacher['hashed_password'],
            education=teacher['education'],
            title=teacher['title'],
            department_id=teacher['department_id'],
        )
    )

for admin in adminData:
    data.append(
        Admin(
            name=admin['name'],
            sex=admin['sex'],
            birthday=admin['birthday'],
            password=admin['password'],
        )
    )

for course in courseData:
    data.append(
        Course(
            id=course['id'],
            name=course['name'],
            credit=course['credit'],
            period=course['period'],
        )
    )

for selectCourse in selectCourseData:
    data.append(
        SelectCourse(
            student_id=selectCourse['student_id'],
            teacher_id=selectCourse['teacher_id'],
            course_id=selectCourse['course_id'],
        )
    )
