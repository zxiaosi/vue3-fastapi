#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 23:00
# @Author : 小四先生
# @desc : 所有数据(被 sqlalchemy_core_initial函数 使用)
"""
  免责声明: 数据来自网络，如有冲突，请联系删除！！！
"""
from datetime import date

userData = [
    {'full_name': '小刘', 'password': '123'},
    {'full_name': '小赵', 'password': '123'},
]

departmentData = [
    {'department_id': '1001', 'department_name': '计算机工程学院', 'department_chairman': '张强', 'department_phone': '123456'},
    {'department_id': '1002', 'department_name': '医学院', 'department_chairman': '马建国', 'department_phone': '123456'},
]

majorData = [
    # 计算机工程学院
    {'major_id': '100101', 'major_name': '计算机科学与技术', 'major_assistant': '钱伟', 'major_phone': '123456',
     'department_id': '1001'},
    {'major_id': '100102', 'major_name': '物联网工程', 'major_assistant': '吴晓红', 'major_phone': '123456',
     'department_id': '1001'},
    {'major_id': '100103', 'major_name': '软件工程技术', 'major_assistant': '柯刚', 'major_phone': '123456',
     'department_id': '1001'},
    # 医学院
    {'major_id': '100201', 'major_name': '中药学专业', 'major_assistant': '赵露', 'major_phone': '123456',
     'department_id': '1002'},
    {'major_id': '100202', 'major_name': '护理学专业', 'major_assistant': '朱壮', 'major_phone': '123456',
     'department_id': '1002'},
    {'major_id': '100203', 'major_name': '针灸推拿学专业', 'major_assistant': '李勇', 'major_phone': '123456',
     'department_id': '1002'},
]

studentData = [
    # Mysql日期可以写成下面语句  ||  date(1999, 9, 9) 为了照顾 Sqlite
    # {'student_id': '1810010101', 'student_name': '王芳', 'student_sex': '女', 'student_birthday': '1999-09-09',
    #  'student_password': '123456', 'major_id': '100101'},

    # 计算机科学与技术
    {'student_id': '1810010101', 'student_name': '王芳', 'student_sex': '女', 'student_birthday': date(1999, 9, 9),
     'student_password': '123456', 'major_id': '100101'},
    {'student_id': '1810010102', 'student_name': '孙悟空', 'student_sex': '男', 'student_birthday': date(1999, 5, 23),
     'student_password': '123456', 'major_id': '100101'},
    {'student_id': '1810010103', 'student_name': '猪悟能', 'student_sex': '男', 'student_birthday': date(1998, 2, 12),
     'student_password': '123456', 'major_id': '100101'},
    {'student_id': '1810010104', 'student_name': '唐三葬', 'student_sex': '男', 'student_birthday': date(2000, 1, 7),
     'student_password': '123456', 'major_id': '100101'},
    {'student_id': '1810010105', 'student_name': '张悟本', 'student_sex': '男', 'student_birthday': date(2000, 3, 29),
     'student_password': '123456', 'major_id': '100101'},
    # 物联网工程
    {'student_id': '1810010201', 'student_name': '宋清江', 'student_sex': '女', 'student_birthday': date(2000, 2, 10),
     'student_password': '123456', 'major_id': '100102'},
    {'student_id': '1810010202', 'student_name': '甄无用', 'student_sex': '男', 'student_birthday': date(1999, 6, 21),
     'student_password': '123456', 'major_id': '100102'},
    {'student_id': '1810010203', 'student_name': '关不胜', 'student_sex': '男', 'student_birthday': date(1999, 7, 19),
     'student_password': '123456', 'major_id': '100102'},
    {'student_id': '1810010204', 'student_name': '秦复明', 'student_sex': '女', 'student_birthday': date(2001, 1, 26),
     'student_password': '123456', 'major_id': '100102'},
    {'student_id': '1810010205', 'student_name': '花繁荣', 'student_sex': '女', 'student_birthday': date(2000, 5, 27),
     'student_password': '123456', 'major_id': '100102'},
    # 软件工程技术
    {'student_id': '1810010301', 'student_name': '柴进门', 'student_sex': '男', 'student_birthday': date(1999, 4, 26),
     'student_password': '123456', 'major_id': '100103'},
    {'student_id': '1810010302', 'student_name': '李天应', 'student_sex': '女', 'student_birthday': date(1999, 6, 4),
     'student_password': '123456', 'major_id': '100103'},
    {'student_id': '1810010303', 'student_name': '董不平', 'student_sex': '男', 'student_birthday': date(1999, 9, 30),
     'student_password': '123456', 'major_id': '100103'},
    {'student_id': '1810010304', 'student_name': '徐宁静', 'student_sex': '女', 'student_birthday': date(2000, 8, 20),
     'student_password': '123456', 'major_id': '100103'},
    {'student_id': '1810010305', 'student_name': '索超越', 'student_sex': '男', 'student_birthday': date(1999, 7, 20),
     'student_password': '123456', 'major_id': '100103'},
    # 中药学专业
    {'student_id': '1810020101', 'student_name': '刘唐氏', 'student_sex': '女', 'student_birthday': date(1999, 1, 17),
     'student_password': '123456', 'major_id': '100201'},
    {'student_id': '1810020102', 'student_name': '李逵悟', 'student_sex': '男', 'student_birthday': date(1999, 5, 13),
     'student_password': '123456', 'major_id': '100201'},
    {'student_id': '1810020103', 'student_name': '阮小三', 'student_sex': '男', 'student_birthday': date(1999, 9, 16),
     'student_password': '123456', 'major_id': '100201'},
    {'student_id': '1810020104', 'student_name': '石秀气', 'student_sex': '女', 'student_birthday': date(2000, 1, 18),
     'student_password': '123456', 'major_id': '100201'},
    {'student_id': '1810020105', 'student_name': '谢宝庆', 'student_sex': '男', 'student_birthday': date(2000, 2, 25),
     'student_password': '123456', 'major_id': '100201'},
    # 护理学专业
    {'student_id': '1810020201', 'student_name': '燕青青', 'student_sex': '女', 'student_birthday': date(2000, 7, 29),
     'student_password': '123456', 'major_id': '100202'},
    {'student_id': '1810020202', 'student_name': '朱文武', 'student_sex': '男', 'student_birthday': date(1999, 2, 12),
     'student_password': '123456', 'major_id': '100202'},
    {'student_id': '1810020203', 'student_name': '鲍旭日', 'student_sex': '男', 'student_birthday': date(1999, 8, 25),
     'student_password': '123456', 'major_id': '100202'},
    {'student_id': '1810020204', 'student_name': '孔明亮', 'student_sex': '女', 'student_birthday': date(1999, 3, 12),
     'student_password': '123456', 'major_id': '100202'},
    {'student_id': '1810020205', 'student_name': '童威猛', 'student_sex': '男', 'student_birthday': date(1999, 4, 16),
     'student_password': '123456', 'major_id': '100202'},
    # 针灸推拿学专业
    {'student_id': '1810020301', 'student_name': '朱富贵', 'student_sex': '男', 'student_birthday': date(1998, 2, 15),
     'student_password': '123456', 'major_id': '100203'},
    {'student_id': '1810020302', 'student_name': '孙大嫂', 'student_sex': '女', 'student_birthday': date(1999, 3, 27),
     'student_password': '123456', 'major_id': '100203'},
    {'student_id': '1810020303', 'student_name': '王小二', 'student_sex': '男', 'student_birthday': date(1999, 6, 28),
     'student_password': '123456', 'major_id': '100203'},
    {'student_id': '1810020304', 'student_name': '白胜利', 'student_sex': '女', 'student_birthday': date(1999, 8, 10),
     'student_password': '123456', 'major_id': '100203'},
    {'student_id': '1810020305', 'student_name': '段金柱', 'student_sex': '男', 'student_birthday': date(1999, 2, 12),
     'student_password': '123456', 'major_id': '100203'},
]

teacherData = [
    # 计算机工程学院
    {'teacher_id': '180101', 'teacher_name': '陈江川', 'teacher_sex': '男', 'teacher_birthday': date(1988, 9, 9),
     'teacher_password': '123456', 'teacher_education': '学士', 'teacher_title': '副教授', 'department_id': '1001'},
    {'teacher_id': '180102', 'teacher_name': '李小平', 'teacher_sex': '男', 'teacher_birthday': date(1993, 8, 17),
     'teacher_password': '123456', 'teacher_education': '硕士', 'teacher_title': '讲师', 'department_id': '1001'},
    {'teacher_id': '180103', 'teacher_name': '赵希明', 'teacher_sex': '女', 'teacher_birthday': date(1988, 3, 28),
     'teacher_password': '123456', 'teacher_education': '博士', 'teacher_title': '教授', 'department_id': '1001'},
    {'teacher_id': '180104', 'teacher_name': '张红', 'teacher_sex': '女', 'teacher_birthday': date(1995, 6, 15),
     'teacher_password': '123456', 'teacher_education': '学士', 'teacher_title': '助教', 'department_id': '1001'},
    # 医学院
    {'teacher_id': '180201', 'teacher_name': '吴小龚', 'teacher_sex': '女', 'teacher_birthday': date(1988, 4, 20),
     'teacher_password': '123456', 'teacher_education': '硕士', 'teacher_title': '讲师', 'department_id': '1002'},
    {'teacher_id': '180202', 'teacher_name': '张进明', 'teacher_sex': '男', 'teacher_birthday': date(1989, 10, 29),
     'teacher_password': '123456', 'teacher_education': '学士', 'teacher_title': '助教', 'department_id': '1002'},
    {'teacher_id': '180203', 'teacher_name': '李历宁', 'teacher_sex': '男', 'teacher_birthday': date(1996, 3, 19),
     'teacher_password': '123456', 'teacher_education': '学士', 'teacher_title': '副教授', 'department_id': '1002'},
]

adminData = [
    {'admin_name': 'admin', 'admin_sex': '男', 'admin_birthday': date(2012, 1, 1), 'admin_password': 'admin'},
]

courseData = [
    {'course_id': '0101', 'course_name': '计算机导论', 'course_credit': 2, 'course_period': 16},
    {'course_id': '0102', 'course_name': '计算机网络', 'course_credit': 2, 'course_period': 16},
    {'course_id': '0103', 'course_name': 'Java', 'course_credit': 4, 'course_period': 16},
    {'course_id': '0104', 'course_name': 'C语言', 'course_credit': 4, 'course_period': 16},
    {'course_id': '0201', 'course_name': '基础化学', 'course_credit': 2, 'course_period': 16},
    {'course_id': '0202', 'course_name': '生理学', 'course_credit': 3, 'course_period': 16},
    {'course_id': '0203', 'course_name': '中医学', 'course_credit': 4, 'course_period': 16},
]

selectCourseData = [
    {'student_id': '1810010101', 'teacher_id': '180101', 'course_id': '0101'},
]
