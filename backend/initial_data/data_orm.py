#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 20:48
# @Author : 小四先生
# @desc : data_core中数据的加工(被 sqlalchemy_orm_initial函数 使用)
from backend.initial_data.data_core import userData, departmentData, majorData, studentData, teacherData, adminData, \
    courseData, selectCourseData
from backend.models.admin import Admin
from backend.models.course import Course
from backend.models.department import Department
from backend.models.major import Major
from backend.models.selectCourse import SelectCourse
from backend.models.student import Student
from backend.models.teacher import Teacher
from backend.models.user import User

data = []

for user in userData:
    data.append(User(full_name=user['full_name'], password=user['password']))

for department in departmentData:
    data.append(
        Department(
            department_id=department['department_id'],
            department_name=department['department_name'],
            department_chairman=department['department_chairman'],
            department_phone=department['department_phone']
        )
    )

for major in majorData:
    data.append(
        Major(
            major_id=major['major_id'],
            major_name=major['major_name'],
            major_assistant=major['major_assistant'],
            major_phone=major['major_phone'],
            department_id=major['department_id']
        )
    )

for student in studentData:
    data.append(
        Student(
            student_id=student['student_id'],
            student_name=student['student_name'],
            student_sex=student['student_sex'],
            student_birthday=student['student_birthday'],
            student_password=student['student_password'],
            major_id=student['major_id'],
        )
    )

for teacher in teacherData:
    data.append(
        Teacher(
            teacher_id=teacher['teacher_id'],
            teacher_name=teacher['teacher_name'],
            teacher_sex=teacher['teacher_sex'],
            teacher_birthday=teacher['teacher_birthday'],
            teacher_password=teacher['teacher_password'],
            teacher_education=teacher['teacher_education'],
            teacher_title=teacher['teacher_title'],
            department_id=teacher['department_id'],
        )
    )

for admin in adminData:
    data.append(
        Admin(
            admin_name=admin['admin_name'],
            admin_sex=admin['admin_sex'],
            admin_birthday=admin['admin_birthday'],
            admin_password=admin['admin_password'],
        )
    )

for course in courseData:
    data.append(
        Course(
            course_id=course['course_id'],
            course_name=course['course_name'],
            course_credit=course['course_credit'],
            course_period=course['course_period'],
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
