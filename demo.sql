/*
 Navicat Premium Data Transfer

 Source Server         : root
 Source Server Type    : MySQL
 Source Server Version : 80031
 Source Host           : localhost:3306
 Source Schema         : demo

 Target Server Type    : MySQL
 Target Server Version : 80031
 File Encoding         : 65001

 Date: 23/05/2023 15:47:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for resource
-- ----------------------------
DROP TABLE IF EXISTS `resource`;
CREATE TABLE `resource`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `name` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '资源名称',
  `level` smallint NOT NULL DEFAULT 0 COMMENT '层级: 0 目录 1 菜单 2 权限',
  `pid` int NOT NULL DEFAULT 0 COMMENT '父节点id',
  `icon` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '图标',
  `menu_url` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '页面路由',
  `request_url` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '请求url',
  `permission_code` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '权限code',
  `is_deleted` smallint NULL DEFAULT 0 COMMENT '是否删除: 0 未删除 1 已删除',
  `create_time` datetime NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of resource
-- ----------------------------
INSERT INTO `resource` VALUES (1, '仪表盘', 1, 0, 'VBr0B.png', '/dashboard', '/', '', 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');
INSERT INTO `resource` VALUES (2, '系统管理', 0, 0, 'VBr0B.png', '/system/index', '/system', 'sys', 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');
INSERT INTO `resource` VALUES (3, '用户管理', 1, 2, 'VBclq.png', '/system/user', '/user', 'sys:user', 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');
INSERT INTO `resource` VALUES (4, '用户列表', 2, 3, NULL, NULL, '/user/list', 'sys:user:list', 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');
INSERT INTO `resource` VALUES (5, '新增用户', 2, 3, NULL, NULL, '/user/add', 'sys:user:add', 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');
INSERT INTO `resource` VALUES (6, '编辑用户', 2, 3, NULL, NULL, '/user/update', 'sys:user:update', 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');
INSERT INTO `resource` VALUES (7, '角色管理', 1, 2, 'VBsBc.png', '/system/role', '/role', 'sys:role', 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');
INSERT INTO `resource` VALUES (8, '资源管理', 1, 2, 'VBr0B.png', '/system/resource', '/resource', 'sys:resource', 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');
INSERT INTO `resource` VALUES (9, '公告通知', 1, 0, 'VBr0B.png', '/notice', '/notice', 'notice', 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');
INSERT INTO `resource` VALUES (10, '日志记录', 1, 0, 'VBr0B.png', '/log', '/log', 'log', 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `name` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '角色名称',
  `code` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '角色code',
  `description` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '角色描述',
  `is_deleted` smallint NULL DEFAULT 0 COMMENT '是否删除: 0 未删除 1 已删除',
  `create_time` datetime NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES (1, '超级管理员', 'ROLE_ADMIN', '管理员', 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');
INSERT INTO `role` VALUES (2, '管理员', 'ROLE_USER', '普通用户', 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');
INSERT INTO `role` VALUES (3, '游客', 'ROLE_GUEST', '普通用户', 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');

-- ----------------------------
-- Table structure for role_resource
-- ----------------------------
DROP TABLE IF EXISTS `role_resource`;
CREATE TABLE `role_resource`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `role_id` int NOT NULL COMMENT '角色id',
  `resource_id` int NOT NULL COMMENT '资源id',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `role_id`(`role_id` ASC) USING BTREE,
  INDEX `resource_id`(`resource_id` ASC) USING BTREE,
  CONSTRAINT `role_resource_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `role_resource_ibfk_2` FOREIGN KEY (`resource_id`) REFERENCES `resource` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role_resource
-- ----------------------------
INSERT INTO `role_resource` VALUES (1, 1, 1);
INSERT INTO `role_resource` VALUES (2, 1, 2);
INSERT INTO `role_resource` VALUES (3, 1, 3);
INSERT INTO `role_resource` VALUES (4, 1, 4);
INSERT INTO `role_resource` VALUES (5, 1, 5);
INSERT INTO `role_resource` VALUES (6, 1, 6);
INSERT INTO `role_resource` VALUES (7, 1, 7);
INSERT INTO `role_resource` VALUES (8, 1, 8);
INSERT INTO `role_resource` VALUES (9, 1, 9);
INSERT INTO `role_resource` VALUES (10, 1, 10);
INSERT INTO `role_resource` VALUES (11, 2, 1);
INSERT INTO `role_resource` VALUES (12, 3, 1);

-- ----------------------------
-- Table structure for sys_log
-- ----------------------------
DROP TABLE IF EXISTS `sys_log`;
CREATE TABLE `sys_log`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `url` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '请求url',
  `method` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '请求方法',
  `ip` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '请求ip',
  `params` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '请求参数',
  `spend_time` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '响应时间',
  `create_time` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_log
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `name` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '用户名',
  `password` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '密码',
  `avatar` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '头像',
  `sex` smallint NULL DEFAULT 0 COMMENT '性别: 0 未知 1 男 2 女',
  `phone` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '手机号',
  `version` int NOT NULL DEFAULT 1 COMMENT '版本号',
  `is_deleted` smallint NULL DEFAULT 0 COMMENT '是否删除: 0 未删除 1 已删除',
  `create_time` datetime NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'admin', '30780cc6f2e56945aaf9c9578c932e22', NULL, 0, NULL, 1, 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');
INSERT INTO `user` VALUES (2, 'user', '30780cc6f2e56945aaf9c9578c932e22', NULL, 1, NULL, 1, 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');
INSERT INTO `user` VALUES (3, 'guest', '30780cc6f2e56945aaf9c9578c932e22', NULL, 2, NULL, 1, 0, '2023-05-23 15:45:24', '2023-05-23 15:45:24');

-- ----------------------------
-- Table structure for user_role
-- ----------------------------
DROP TABLE IF EXISTS `user_role`;
CREATE TABLE `user_role`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `user_id` int NOT NULL COMMENT '用户id',
  `role_id` int NOT NULL COMMENT '角色id',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_id`(`user_id` ASC) USING BTREE,
  INDEX `role_id`(`role_id` ASC) USING BTREE,
  CONSTRAINT `user_role_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `user_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_role
-- ----------------------------
INSERT INTO `user_role` VALUES (1, 1, 1);
INSERT INTO `user_role` VALUES (2, 2, 2);
INSERT INTO `user_role` VALUES (3, 3, 3);

SET FOREIGN_KEY_CHECKS = 1;
