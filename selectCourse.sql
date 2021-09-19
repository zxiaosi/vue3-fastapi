/*
 Navicat Premium Data Transfer

 Source Server         : root
 Source Server Type    : MySQL
 Source Server Version : 50734
 Source Host           : localhost:3306
 Source Schema         : courser_selection

 Target Server Type    : MySQL
 Target Server Version : 50734
 File Encoding         : 65001

 Date: 19/09/2021 21:53:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for administrator
-- ----------------------------
DROP TABLE IF EXISTS `administrator`;
CREATE TABLE `administrator`  (
  `adminNo` int(2) NOT NULL,
  `adminName` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `adminSex` enum('男','女') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `adminBirthday` datetime(0) NOT NULL,
  `adminPassword` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`adminNo`) USING BTREE,
  UNIQUE INDEX `adminName`(`adminName`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of administrator
-- ----------------------------
INSERT INTO `administrator` VALUES (1, 'admin', '男', '1989-01-01 00:00:00', '123456');

-- ----------------------------
-- Table structure for control
-- ----------------------------
DROP TABLE IF EXISTS `control`;
CREATE TABLE `control`  (
  `ifTakeCourse` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ifInputGrade` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of control
-- ----------------------------

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `courseId` int(4) NOT NULL,
  `courseName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `courseCredit` smallint(6) NOT NULL,
  `courseClass` smallint(6) NOT NULL,
  PRIMARY KEY (`courseId`) USING BTREE,
  UNIQUE INDEX `courseName`(`courseName`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES (1010, 'C语言', 4, 4);
INSERT INTO `course` VALUES (1011, 'Java', 4, 2);
INSERT INTO `course` VALUES (1012, '数据库', 4, 2);
INSERT INTO `course` VALUES (1013, '计算机网络', 2, 2);
INSERT INTO `course` VALUES (1014, '计算机组成原理', 2, 2);

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department`  (
  `deptId` int(4) NOT NULL,
  `deptName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `deptChairman` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `deptTel` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`deptId`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of department
-- ----------------------------
INSERT INTO `department` VALUES (1001, '计算机工程学院', '计工', '1234567890');
INSERT INTO `department` VALUES (1002, '外国语学院', '外语', '1234567890');

-- ----------------------------
-- Table structure for major
-- ----------------------------
DROP TABLE IF EXISTS `major`;
CREATE TABLE `major`  (
  `majorId` int(6) NOT NULL,
  `majorName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `majorAssistant` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `majorTel` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `deptId` int(4) NOT NULL,
  PRIMARY KEY (`majorId`) USING BTREE,
  INDEX `Major_fk_department`(`deptId`) USING BTREE,
  CONSTRAINT `Major_fk_department` FOREIGN KEY (`deptId`) REFERENCES `department` (`deptId`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of major
-- ----------------------------
INSERT INTO `major` VALUES (202101, '计算机科学与技术', '计科', '1234567890', 1001);
INSERT INTO `major` VALUES (202102, '物联网', '物联网', '1234567890', 1001);
INSERT INTO `major` VALUES (202103, '软件工程', '软件', '1234567890', 1001);
INSERT INTO `major` VALUES (202104, '应用英语', '应用', '1234567890', 1002);
INSERT INTO `major` VALUES (202105, '商务英语', '商务', '1234567890', 1002);

-- ----------------------------
-- Table structure for selectcourse
-- ----------------------------
DROP TABLE IF EXISTS `selectcourse`;
CREATE TABLE `selectcourse`  (
  `stuNo` int(10) NOT NULL,
  `courseId` int(8) NOT NULL,
  `teachNo` int(10) NOT NULL,
  `grade` smallint(6) NULL DEFAULT NULL,
  INDEX `selectCourse_fk_student`(`stuNo`) USING BTREE,
  INDEX `selectCourse_fk_course`(`courseId`) USING BTREE,
  INDEX `selectCourse_fk_teacher`(`teachNo`) USING BTREE,
  CONSTRAINT `selectCourse_fk_course` FOREIGN KEY (`courseId`) REFERENCES `course` (`courseId`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `selectCourse_fk_student` FOREIGN KEY (`stuNo`) REFERENCES `student` (`stuNo`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `selectCourse_fk_teacher` FOREIGN KEY (`teachNo`) REFERENCES `teacher` (`teachNo`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of selectcourse
-- ----------------------------
INSERT INTO `selectcourse` VALUES (2021010001, 1010, 2021100101, NULL);
INSERT INTO `selectcourse` VALUES (2021010002, 1010, 2021100101, NULL);
INSERT INTO `selectcourse` VALUES (2021010003, 1011, 2021100101, NULL);

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `stuNo` int(10) NOT NULL,
  `stuName` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stuSex` enum('男','女') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stuBirthday` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  `stuPassword` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `majorId` int(6) NOT NULL,
  PRIMARY KEY (`stuNo`) USING BTREE,
  UNIQUE INDEX `stuName`(`stuName`) USING BTREE,
  INDEX `student_fk_Major`(`majorId`) USING BTREE,
  CONSTRAINT `student_fk_Major` FOREIGN KEY (`majorId`) REFERENCES `major` (`majorId`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (2021010001, '小一', '女', '1999-01-01 00:00:00', '123456', 202101);
INSERT INTO `student` VALUES (2021010002, '小二', '男', '1999-02-01 00:00:00', '123456', 202101);
INSERT INTO `student` VALUES (2021010003, '小三', '男', '2000-03-01 00:00:00', '123456', 202101);
INSERT INTO `student` VALUES (2021020001, '小四', '女', '1999-04-01 00:00:00', '123456', 202102);
INSERT INTO `student` VALUES (2021020002, '小五', '男', '2000-05-01 00:00:00', '123456', 202102);
INSERT INTO `student` VALUES (2021020003, '小六', '男', '1999-06-01 00:00:00', '123456', 202102);
INSERT INTO `student` VALUES (2021030001, '小七', '女', '2000-07-01 00:00:00', '123456', 202103);
INSERT INTO `student` VALUES (2021030002, '小八', '男', '2000-08-01 00:00:00', '123456', 202103);
INSERT INTO `student` VALUES (2021030003, '小九', '女', '1999-09-01 00:00:00', '123456', 202103);
INSERT INTO `student` VALUES (2021040001, '大一', '女', '1999-10-01 00:00:00', '123456', 202103);
INSERT INTO `student` VALUES (2021040002, '大二', '女', '2000-11-01 00:00:00', '123456', 202103);
INSERT INTO `student` VALUES (2021040003, '大三', '女', '1999-12-01 00:00:00', '123456', 202103);
INSERT INTO `student` VALUES (2021050001, '大四', '女', '2000-01-01 00:00:00', '123456', 202103);
INSERT INTO `student` VALUES (2021050002, '大五', '女', '1999-02-01 00:00:00', '123456', 202103);
INSERT INTO `student` VALUES (2021050003, '大六', '女', '1999-03-01 00:00:00', '123456', 202103);

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher`  (
  `teachNo` int(10) NOT NULL,
  `teachName` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `teachSex` enum('男','女') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `teachBirthday` datetime(0) NOT NULL,
  `teachPassword` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `teacheducation` char(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `teachTitle` varchar(6) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `deptId` int(8) NOT NULL,
  PRIMARY KEY (`teachNo`) USING BTREE,
  UNIQUE INDEX `teachName`(`teachName`) USING BTREE,
  INDEX `teacher_fk_deptId`(`deptId`) USING BTREE,
  CONSTRAINT `teacher_fk_deptId` FOREIGN KEY (`deptId`) REFERENCES `department` (`deptId`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES (2021100101, '赵老师', '男', '1989-01-01 00:00:00', '123456', '博士', '教授', 1001);
INSERT INTO `teacher` VALUES (2021100102, '钱老师', '女', '1995-01-01 00:00:00', '123456', '学士', '助教', 1002);
INSERT INTO `teacher` VALUES (2021100103, '孙老师', '男', '1992-01-01 00:00:00', '123456', '硕士', '讲师', 1001);
INSERT INTO `teacher` VALUES (2021100104, '李老师', '男', '1993-01-01 00:00:00', '123456', '硕士', '讲师', 1001);
INSERT INTO `teacher` VALUES (2021100105, '周老师', '女', '1990-01-01 00:00:00', '123456', '硕士', '副教授', 1002);
INSERT INTO `teacher` VALUES (2021100106, '田老师', '女', '1988-01-01 00:00:00', '123456', '博士', '教授', 1002);

SET FOREIGN_KEY_CHECKS = 1;
