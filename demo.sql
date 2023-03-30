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

 Date: 31/03/2023 00:21:48
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
INSERT INTO `resource` VALUES (1, '仪表盘', 1, 0, 'VBr0B.png', '/dashboard', '/', '', 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');
INSERT INTO `resource` VALUES (2, '系统管理', 0, 0, 'VBr0B.png', '/system/index', '/system', 'sys', 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');
INSERT INTO `resource` VALUES (3, '用户管理', 1, 2, 'VBclq.png', '/system/user', '/user', 'sys:user', 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');
INSERT INTO `resource` VALUES (4, '用户列表', 2, 3, NULL, NULL, '/user/list', 'sys:user:list', 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');
INSERT INTO `resource` VALUES (5, '新增用户', 2, 3, NULL, NULL, '/user/add', 'sys:user:add', 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');
INSERT INTO `resource` VALUES (6, '编辑用户', 2, 3, NULL, NULL, '/user/update', 'sys:user:update', 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');
INSERT INTO `resource` VALUES (7, '角色管理', 1, 2, 'VBsBc.png', '/system/role', '/role', 'sys:role', 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');
INSERT INTO `resource` VALUES (8, '资源管理', 1, 2, 'VBr0B.png', '/system/resource', '/resource', 'sys:resource', 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');
INSERT INTO `resource` VALUES (9, '公告通知', 1, 0, 'VBr0B.png', '/notice', '/notice', 'notice', 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');
INSERT INTO `resource` VALUES (10, '日志记录', 1, 0, 'VBr0B.png', '/log', '/log', 'log', 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');

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
INSERT INTO `role` VALUES (1, '超级管理员', 'ROLE_ADMIN', '管理员', 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');
INSERT INTO `role` VALUES (2, '管理员', 'ROLE_USER', '普通用户', 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');
INSERT INTO `role` VALUES (3, '游客', 'ROLE_GUEST', '普通用户', 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');

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
) ENGINE = InnoDB AUTO_INCREMENT = 63 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_log
-- ----------------------------
INSERT INTO `sys_log` VALUES (1, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.034555673599243164', '2023-03-28 18:35:37');
INSERT INTO `sys_log` VALUES (2, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.047675132751464844', '2023-03-28 18:35:37');
INSERT INTO `sys_log` VALUES (3, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0071756839752197266', '2023-03-28 18:35:37');
INSERT INTO `sys_log` VALUES (4, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004549503326416016', '2023-03-28 18:35:40');
INSERT INTO `sys_log` VALUES (5, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006001949310302734', '2023-03-28 18:35:41');
INSERT INTO `sys_log` VALUES (6, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.007854461669921875', '2023-03-28 18:35:45');
INSERT INTO `sys_log` VALUES (7, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005073070526123047', '2023-03-28 18:35:46');
INSERT INTO `sys_log` VALUES (8, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.007328510284423828', '2023-03-28 18:35:54');
INSERT INTO `sys_log` VALUES (9, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005034685134887695', '2023-03-28 18:35:59');
INSERT INTO `sys_log` VALUES (10, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006299018859863281', '2023-03-28 18:36:16');
INSERT INTO `sys_log` VALUES (11, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005858898162841797', '2023-03-28 18:36:17');
INSERT INTO `sys_log` VALUES (12, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0052547454833984375', '2023-03-28 18:36:17');
INSERT INTO `sys_log` VALUES (13, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005524873733520508', '2023-03-28 18:36:18');
INSERT INTO `sys_log` VALUES (14, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005842685699462891', '2023-03-28 18:36:19');
INSERT INTO `sys_log` VALUES (15, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'2\', \'page_size\': \'10\'}', '0.004248857498168945', '2023-03-28 18:36:20');
INSERT INTO `sys_log` VALUES (16, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'2\', \'page_size\': \'10\'}', '0.006000518798828125', '2023-03-28 18:36:23');
INSERT INTO `sys_log` VALUES (17, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'2\', \'page_size\': \'10\'}', '0.005468845367431641', '2023-03-28 18:36:24');
INSERT INTO `sys_log` VALUES (18, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005579233169555664', '2023-03-28 18:37:47');
INSERT INTO `sys_log` VALUES (19, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005415201187133789', '2023-03-28 18:37:50');
INSERT INTO `sys_log` VALUES (20, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'2\', \'page_size\': \'10\'}', '0.005994081497192383', '2023-03-28 18:37:51');
INSERT INTO `sys_log` VALUES (21, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004884958267211914', '2023-03-28 18:39:16');
INSERT INTO `sys_log` VALUES (22, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'2\', \'page_size\': \'10\'}', '0.004363059997558594', '2023-03-28 18:39:17');
INSERT INTO `sys_log` VALUES (23, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'3\', \'page_size\': \'10\'}', '0.004997730255126953', '2023-03-28 18:39:18');
INSERT INTO `sys_log` VALUES (24, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00500035285949707', '2023-03-28 18:39:20');
INSERT INTO `sys_log` VALUES (25, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'2\', \'page_size\': \'10\'}', '0.005006074905395508', '2023-03-28 18:39:21');
INSERT INTO `sys_log` VALUES (26, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006502389907836914', '2023-03-28 18:40:01');
INSERT INTO `sys_log` VALUES (27, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0042836666107177734', '2023-03-28 18:43:38');
INSERT INTO `sys_log` VALUES (28, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'2\', \'page_size\': \'10\'}', '0.0047681331634521484', '2023-03-28 18:43:38');
INSERT INTO `sys_log` VALUES (29, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005333900451660156', '2023-03-28 18:43:41');
INSERT INTO `sys_log` VALUES (30, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006102085113525391', '2023-03-28 18:43:43');
INSERT INTO `sys_log` VALUES (31, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0064868927001953125', '2023-03-28 18:44:01');
INSERT INTO `sys_log` VALUES (32, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0050008296966552734', '2023-03-28 18:44:03');
INSERT INTO `sys_log` VALUES (33, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0051386356353759766', '2023-03-28 18:45:43');
INSERT INTO `sys_log` VALUES (34, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00503087043762207', '2023-03-28 18:45:44');
INSERT INTO `sys_log` VALUES (35, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'2\', \'page_size\': \'10\'}', '0.00646519660949707', '2023-03-28 18:45:46');
INSERT INTO `sys_log` VALUES (36, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'3\', \'page_size\': \'10\'}', '0.004982948303222656', '2023-03-28 18:45:47');
INSERT INTO `sys_log` VALUES (37, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'4\', \'page_size\': \'10\'}', '0.004995822906494141', '2023-03-28 18:45:48');
INSERT INTO `sys_log` VALUES (38, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006155967712402344', '2023-03-28 18:45:49');
INSERT INTO `sys_log` VALUES (39, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'2\', \'page_size\': \'10\'}', '0.005001068115234375', '2023-03-28 18:45:50');
INSERT INTO `sys_log` VALUES (40, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'3\', \'page_size\': \'10\'}', '0.0029954910278320312', '2023-03-28 18:45:51');
INSERT INTO `sys_log` VALUES (41, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'4\', \'page_size\': \'10\'}', '0.0039980411529541016', '2023-03-28 18:45:52');
INSERT INTO `sys_log` VALUES (42, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'3\', \'page_size\': \'10\'}', '0.0057942867279052734', '2023-03-28 18:45:53');
INSERT INTO `sys_log` VALUES (43, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'5\', \'page_size\': \'10\'}', '0.005004405975341797', '2023-03-28 18:45:54');
INSERT INTO `sys_log` VALUES (44, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0055103302001953125', '2023-03-28 18:45:55');
INSERT INTO `sys_log` VALUES (45, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'5\', \'page_size\': \'10\'}', '0.00402522087097168', '2023-03-28 18:46:09');
INSERT INTO `sys_log` VALUES (46, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005524873733520508', '2023-03-28 18:46:13');
INSERT INTO `sys_log` VALUES (47, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'3\', \'page_size\': \'10\'}', '0.006000041961669922', '2023-03-28 18:46:15');
INSERT INTO `sys_log` VALUES (48, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'4\', \'page_size\': \'10\'}', '0.005005598068237305', '2023-03-28 18:46:21');
INSERT INTO `sys_log` VALUES (49, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'5\', \'page_size\': \'10\'}', '0.005997180938720703', '2023-03-28 18:46:23');
INSERT INTO `sys_log` VALUES (50, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006192445755004883', '2023-03-28 18:46:49');
INSERT INTO `sys_log` VALUES (51, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'2\', \'page_size\': \'10\'}', '0.005004167556762695', '2023-03-28 18:46:55');
INSERT INTO `sys_log` VALUES (52, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0051801204681396484', '2023-03-28 18:46:57');
INSERT INTO `sys_log` VALUES (53, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004996776580810547', '2023-03-28 18:47:04');
INSERT INTO `sys_log` VALUES (54, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005944013595581055', '2023-03-28 18:47:34');
INSERT INTO `sys_log` VALUES (55, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'2\', \'page_size\': \'10\'}', '0.004917144775390625', '2023-03-28 18:47:36');
INSERT INTO `sys_log` VALUES (56, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'3\', \'page_size\': \'10\'}', '0.005551815032958984', '2023-03-28 18:47:37');
INSERT INTO `sys_log` VALUES (57, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'4\', \'page_size\': \'10\'}', '0.005000114440917969', '2023-03-28 18:47:38');
INSERT INTO `sys_log` VALUES (58, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'5\', \'page_size\': \'10\'}', '0.004696846008300781', '2023-03-28 18:47:39');
INSERT INTO `sys_log` VALUES (59, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'6\', \'page_size\': \'10\'}', '0.005323171615600586', '2023-03-28 18:47:39');
INSERT INTO `sys_log` VALUES (60, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004550933837890625', '2023-03-28 18:47:50');
INSERT INTO `sys_log` VALUES (61, '/api/user/login', 'POST', '127.0.0.1', '{\'name\': \'admin\', \'password\': \'FWRQGPNB9wiqaGY7Uh4FTi/Jj9xVAIcWsl4HIkGboYgKpCTGu2NIEYq82zAQ31ZV6JZTxYNWh1fznMDsbykjc1zMJD9ZJhWcIoW3LvRt7YZTzvJCGUKjXnzR3fxsHOC9O5DgE1LYYAjK6I6iJUy5k92sqmtANyshq+rK/dZgjXU=\'}', '0.07107138633728027', '2023-03-30 13:32:08');
INSERT INTO `sys_log` VALUES (62, '/api/log/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.01191258430480957', '2023-03-30 13:32:23');
INSERT INTO `sys_log` VALUES (63, '/api/user/logout', 'POST', '127.0.0.1', '{}', '0.0029964447021484375', '2023-03-30 13:33:35');
INSERT INTO `sys_log` VALUES (64, '/api/user/login', 'POST', '127.0.0.1', '{\'name\': \'admin\', \'password\': \'L8d3NJ5KYHEwXvw6MxLo7EPrLbYZ/MFKxOEP55wX5g4rQ+fhFhxB6+d9KW5YOYTdSJy3Th+BPsej6aP9ONmVatYom1FZh0U5iKs90BICKByx7Kk4UKm7o3qbdduT/0pOt9IuErt2eaKMPB1IfqeFgflOnnx7vp7yDjCywKO4Rw4=\'}', '0.005999565124511719', '2023-03-30 13:33:36');
INSERT INTO `sys_log` VALUES (65, '/api/user/menu', 'GET', '127.0.0.1', '{}', '0.008241653442382812', '2023-03-30 13:33:36');
INSERT INTO `sys_log` VALUES (66, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0070264339447021484', '2023-03-30 13:33:38');
INSERT INTO `sys_log` VALUES (67, '/api/user/logout', 'POST', '127.0.0.1', '{}', '0.023718833923339844', '2023-03-30 13:33:48');
INSERT INTO `sys_log` VALUES (68, '/api/user/login', 'POST', '127.0.0.1', '{\'name\': \'admin\', \'password\': \'OncTA2Njdgsl7XMAuX5iXPJHwH5ZH6tyCZZrhQGgVZzWBY5qXGzBvxf2uFK4Rct5bO1w6AJ1uyN6V6D2cTivqi7iNOMFHsA5egzT3VcXGOziByZ/u0a6PFX4O+InZweuI7gYI7Y6v7Mi6ksTBeuzAUSHeiSSLP/mipB1g1YPEIw=\'}', '0.01718616485595703', '2023-03-30 13:33:50');
INSERT INTO `sys_log` VALUES (69, '/api/user/menu', 'GET', '127.0.0.1', '{}', '0.0059986114501953125', '2023-03-30 13:33:50');
INSERT INTO `sys_log` VALUES (70, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00831913948059082', '2023-03-30 13:33:52');
INSERT INTO `sys_log` VALUES (71, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006628513336181641', '2023-03-30 13:34:48');
INSERT INTO `sys_log` VALUES (72, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.02986907958984375', '2023-03-30 13:35:58');
INSERT INTO `sys_log` VALUES (73, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.008301496505737305', '2023-03-30 13:39:15');
INSERT INTO `sys_log` VALUES (74, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005412101745605469', '2023-03-30 13:39:18');
INSERT INTO `sys_log` VALUES (75, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004996299743652344', '2023-03-30 14:01:38');
INSERT INTO `sys_log` VALUES (76, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00500798225402832', '2023-03-30 14:01:42');
INSERT INTO `sys_log` VALUES (77, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005346059799194336', '2023-03-30 14:01:54');
INSERT INTO `sys_log` VALUES (78, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004996299743652344', '2023-03-30 14:02:36');
INSERT INTO `sys_log` VALUES (79, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006521701812744141', '2023-03-30 14:04:09');
INSERT INTO `sys_log` VALUES (80, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005538225173950195', '2023-03-30 14:04:47');
INSERT INTO `sys_log` VALUES (81, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006063699722290039', '2023-03-30 14:04:56');
INSERT INTO `sys_log` VALUES (82, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005443572998046875', '2023-03-30 14:22:16');
INSERT INTO `sys_log` VALUES (83, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0066683292388916016', '2023-03-30 14:51:02');
INSERT INTO `sys_log` VALUES (84, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006092548370361328', '2023-03-30 14:51:48');
INSERT INTO `sys_log` VALUES (85, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.007123231887817383', '2023-03-30 14:51:56');
INSERT INTO `sys_log` VALUES (86, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004830837249755859', '2023-03-30 14:52:47');
INSERT INTO `sys_log` VALUES (87, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005228281021118164', '2023-03-30 14:52:49');
INSERT INTO `sys_log` VALUES (88, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0060024261474609375', '2023-03-30 14:53:00');
INSERT INTO `sys_log` VALUES (89, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006029844284057617', '2023-03-30 14:53:02');
INSERT INTO `sys_log` VALUES (90, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00613713264465332', '2023-03-30 14:53:16');
INSERT INTO `sys_log` VALUES (91, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005114555358886719', '2023-03-30 14:53:31');
INSERT INTO `sys_log` VALUES (92, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006426095962524414', '2023-03-30 14:54:15');
INSERT INTO `sys_log` VALUES (93, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006638050079345703', '2023-03-30 14:54:17');
INSERT INTO `sys_log` VALUES (94, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.007028818130493164', '2023-03-30 14:54:28');
INSERT INTO `sys_log` VALUES (95, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005505561828613281', '2023-03-30 14:57:19');
INSERT INTO `sys_log` VALUES (96, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005219459533691406', '2023-03-30 14:57:21');
INSERT INTO `sys_log` VALUES (97, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0073680877685546875', '2023-03-30 14:58:44');
INSERT INTO `sys_log` VALUES (98, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005751848220825195', '2023-03-30 14:58:46');
INSERT INTO `sys_log` VALUES (99, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0060291290283203125', '2023-03-30 14:59:55');
INSERT INTO `sys_log` VALUES (100, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005090236663818359', '2023-03-30 14:59:58');
INSERT INTO `sys_log` VALUES (101, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0050356388092041016', '2023-03-30 15:00:10');
INSERT INTO `sys_log` VALUES (102, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0070705413818359375', '2023-03-30 15:00:11');
INSERT INTO `sys_log` VALUES (103, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005744457244873047', '2023-03-30 15:00:19');
INSERT INTO `sys_log` VALUES (104, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006599903106689453', '2023-03-30 15:00:20');
INSERT INTO `sys_log` VALUES (105, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005756855010986328', '2023-03-30 15:00:21');
INSERT INTO `sys_log` VALUES (106, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006592988967895508', '2023-03-30 15:12:02');
INSERT INTO `sys_log` VALUES (107, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006398439407348633', '2023-03-30 15:12:03');
INSERT INTO `sys_log` VALUES (108, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00529170036315918', '2023-03-30 15:12:49');
INSERT INTO `sys_log` VALUES (109, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006591081619262695', '2023-03-30 15:12:55');
INSERT INTO `sys_log` VALUES (110, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0057353973388671875', '2023-03-30 15:12:56');
INSERT INTO `sys_log` VALUES (111, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005508899688720703', '2023-03-30 15:12:57');
INSERT INTO `sys_log` VALUES (112, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00700688362121582', '2023-03-30 15:13:04');
INSERT INTO `sys_log` VALUES (113, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004434108734130859', '2023-03-30 15:13:09');
INSERT INTO `sys_log` VALUES (114, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005036115646362305', '2023-03-30 15:13:10');
INSERT INTO `sys_log` VALUES (115, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006686687469482422', '2023-03-30 15:14:21');
INSERT INTO `sys_log` VALUES (116, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005106925964355469', '2023-03-30 15:16:27');
INSERT INTO `sys_log` VALUES (117, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006049394607543945', '2023-03-30 15:17:19');
INSERT INTO `sys_log` VALUES (118, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005731344223022461', '2023-03-30 15:17:21');
INSERT INTO `sys_log` VALUES (119, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005347013473510742', '2023-03-30 15:18:09');
INSERT INTO `sys_log` VALUES (120, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005013704299926758', '2023-03-30 15:18:43');
INSERT INTO `sys_log` VALUES (121, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.007501840591430664', '2023-03-30 15:20:04');
INSERT INTO `sys_log` VALUES (122, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005063533782958984', '2023-03-30 15:20:05');
INSERT INTO `sys_log` VALUES (123, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005196332931518555', '2023-03-30 15:21:29');
INSERT INTO `sys_log` VALUES (124, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004599332809448242', '2023-03-30 15:22:00');
INSERT INTO `sys_log` VALUES (125, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0052869319915771484', '2023-03-30 15:23:38');
INSERT INTO `sys_log` VALUES (126, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005069255828857422', '2023-03-30 15:23:52');
INSERT INTO `sys_log` VALUES (127, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0065915584564208984', '2023-03-30 15:23:52');
INSERT INTO `sys_log` VALUES (128, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006493806838989258', '2023-03-30 15:24:26');
INSERT INTO `sys_log` VALUES (129, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005463123321533203', '2023-03-30 15:30:10');
INSERT INTO `sys_log` VALUES (130, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00689697265625', '2023-03-30 15:30:11');
INSERT INTO `sys_log` VALUES (131, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005711793899536133', '2023-03-30 15:30:14');
INSERT INTO `sys_log` VALUES (132, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005901813507080078', '2023-03-30 15:30:37');
INSERT INTO `sys_log` VALUES (133, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004999399185180664', '2023-03-30 15:30:57');
INSERT INTO `sys_log` VALUES (134, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005999326705932617', '2023-03-30 15:30:59');
INSERT INTO `sys_log` VALUES (135, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005627870559692383', '2023-03-30 15:31:44');
INSERT INTO `sys_log` VALUES (136, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005838871002197266', '2023-03-30 15:31:47');
INSERT INTO `sys_log` VALUES (137, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006724834442138672', '2023-03-30 15:31:53');
INSERT INTO `sys_log` VALUES (138, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0052013397216796875', '2023-03-30 15:31:54');
INSERT INTO `sys_log` VALUES (139, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005024433135986328', '2023-03-30 15:31:55');
INSERT INTO `sys_log` VALUES (140, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.007082939147949219', '2023-03-30 15:32:17');
INSERT INTO `sys_log` VALUES (141, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00602269172668457', '2023-03-30 15:32:40');
INSERT INTO `sys_log` VALUES (142, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005423307418823242', '2023-03-30 15:33:12');
INSERT INTO `sys_log` VALUES (143, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006343841552734375', '2023-03-30 15:33:14');
INSERT INTO `sys_log` VALUES (144, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005051136016845703', '2023-03-30 15:33:20');
INSERT INTO `sys_log` VALUES (145, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006348848342895508', '2023-03-30 15:33:29');
INSERT INTO `sys_log` VALUES (146, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0050089359283447266', '2023-03-30 15:33:50');
INSERT INTO `sys_log` VALUES (147, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004664897918701172', '2023-03-30 15:33:56');
INSERT INTO `sys_log` VALUES (148, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0055272579193115234', '2023-03-30 15:34:25');
INSERT INTO `sys_log` VALUES (149, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.007208824157714844', '2023-03-30 15:35:18');
INSERT INTO `sys_log` VALUES (150, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0050201416015625', '2023-03-30 15:35:42');
INSERT INTO `sys_log` VALUES (151, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005006074905395508', '2023-03-30 15:35:43');
INSERT INTO `sys_log` VALUES (152, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006413698196411133', '2023-03-30 15:36:00');
INSERT INTO `sys_log` VALUES (153, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005171298980712891', '2023-03-30 15:36:05');
INSERT INTO `sys_log` VALUES (154, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004809141159057617', '2023-03-30 15:36:23');
INSERT INTO `sys_log` VALUES (155, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0057430267333984375', '2023-03-30 15:37:07');
INSERT INTO `sys_log` VALUES (156, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004485368728637695', '2023-03-30 15:37:09');
INSERT INTO `sys_log` VALUES (157, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0057790279388427734', '2023-03-30 15:39:07');
INSERT INTO `sys_log` VALUES (158, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005934953689575195', '2023-03-30 15:39:09');
INSERT INTO `sys_log` VALUES (159, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004994869232177734', '2023-03-30 15:40:56');
INSERT INTO `sys_log` VALUES (160, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005507946014404297', '2023-03-30 15:40:58');
INSERT INTO `sys_log` VALUES (161, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005989551544189453', '2023-03-30 15:41:53');
INSERT INTO `sys_log` VALUES (162, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006299495697021484', '2023-03-30 15:42:08');
INSERT INTO `sys_log` VALUES (163, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006227016448974609', '2023-03-30 15:42:11');
INSERT INTO `sys_log` VALUES (164, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0055735111236572266', '2023-03-30 15:42:20');
INSERT INTO `sys_log` VALUES (165, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.008083820343017578', '2023-03-30 15:44:32');
INSERT INTO `sys_log` VALUES (166, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006237506866455078', '2023-03-30 15:44:33');
INSERT INTO `sys_log` VALUES (167, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0057337284088134766', '2023-03-30 15:44:39');
INSERT INTO `sys_log` VALUES (168, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005026102066040039', '2023-03-30 15:44:50');
INSERT INTO `sys_log` VALUES (169, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005148887634277344', '2023-03-30 15:44:51');
INSERT INTO `sys_log` VALUES (170, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005648136138916016', '2023-03-30 15:53:06');
INSERT INTO `sys_log` VALUES (171, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00652623176574707', '2023-03-30 15:54:01');
INSERT INTO `sys_log` VALUES (172, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006048917770385742', '2023-03-30 15:54:13');
INSERT INTO `sys_log` VALUES (173, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004471540451049805', '2023-03-30 15:56:07');
INSERT INTO `sys_log` VALUES (174, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004510164260864258', '2023-03-30 15:56:10');
INSERT INTO `sys_log` VALUES (175, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004765748977661133', '2023-03-30 15:56:44');
INSERT INTO `sys_log` VALUES (176, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005188703536987305', '2023-03-30 15:57:12');
INSERT INTO `sys_log` VALUES (177, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0050127506256103516', '2023-03-30 15:58:10');
INSERT INTO `sys_log` VALUES (178, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0050029754638671875', '2023-03-30 15:58:13');
INSERT INTO `sys_log` VALUES (179, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005532264709472656', '2023-03-30 15:59:01');
INSERT INTO `sys_log` VALUES (180, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005248546600341797', '2023-03-30 15:59:08');
INSERT INTO `sys_log` VALUES (181, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005183219909667969', '2023-03-30 15:59:09');
INSERT INTO `sys_log` VALUES (182, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005021810531616211', '2023-03-30 15:59:53');
INSERT INTO `sys_log` VALUES (183, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0048732757568359375', '2023-03-30 15:59:55');
INSERT INTO `sys_log` VALUES (184, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00504755973815918', '2023-03-30 16:01:23');
INSERT INTO `sys_log` VALUES (185, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006410121917724609', '2023-03-30 16:01:26');
INSERT INTO `sys_log` VALUES (186, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006689548492431641', '2023-03-30 16:01:44');
INSERT INTO `sys_log` VALUES (187, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005990266799926758', '2023-03-30 16:01:45');
INSERT INTO `sys_log` VALUES (188, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0060312747955322266', '2023-03-30 16:02:28');
INSERT INTO `sys_log` VALUES (189, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0055463314056396484', '2023-03-30 16:02:41');
INSERT INTO `sys_log` VALUES (190, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006063699722290039', '2023-03-30 16:02:42');
INSERT INTO `sys_log` VALUES (191, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0056269168853759766', '2023-03-30 16:03:00');
INSERT INTO `sys_log` VALUES (192, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005008220672607422', '2023-03-30 16:03:24');
INSERT INTO `sys_log` VALUES (193, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006587028503417969', '2023-03-30 16:03:54');
INSERT INTO `sys_log` VALUES (194, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0056476593017578125', '2023-03-30 16:03:56');
INSERT INTO `sys_log` VALUES (195, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005012989044189453', '2023-03-30 16:04:28');
INSERT INTO `sys_log` VALUES (196, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0067005157470703125', '2023-03-30 16:04:46');
INSERT INTO `sys_log` VALUES (197, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005524158477783203', '2023-03-30 16:04:49');
INSERT INTO `sys_log` VALUES (198, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005543708801269531', '2023-03-30 16:06:16');
INSERT INTO `sys_log` VALUES (199, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.007310152053833008', '2023-03-30 16:06:40');
INSERT INTO `sys_log` VALUES (200, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006555318832397461', '2023-03-30 16:06:55');
INSERT INTO `sys_log` VALUES (201, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00600433349609375', '2023-03-30 16:06:56');
INSERT INTO `sys_log` VALUES (202, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004854917526245117', '2023-03-30 16:06:58');
INSERT INTO `sys_log` VALUES (203, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006881237030029297', '2023-03-30 16:07:42');
INSERT INTO `sys_log` VALUES (204, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004885435104370117', '2023-03-30 16:07:44');
INSERT INTO `sys_log` VALUES (205, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.007282733917236328', '2023-03-30 16:08:10');
INSERT INTO `sys_log` VALUES (206, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00500178337097168', '2023-03-30 16:08:12');
INSERT INTO `sys_log` VALUES (207, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005026102066040039', '2023-03-30 16:08:24');
INSERT INTO `sys_log` VALUES (208, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005772590637207031', '2023-03-30 16:08:27');
INSERT INTO `sys_log` VALUES (209, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0055887699127197266', '2023-03-30 16:08:29');
INSERT INTO `sys_log` VALUES (210, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005998849868774414', '2023-03-30 16:08:32');
INSERT INTO `sys_log` VALUES (211, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005682706832885742', '2023-03-30 16:08:33');
INSERT INTO `sys_log` VALUES (212, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00507354736328125', '2023-03-30 16:09:27');
INSERT INTO `sys_log` VALUES (213, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0060272216796875', '2023-03-30 16:09:28');
INSERT INTO `sys_log` VALUES (214, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005026817321777344', '2023-03-30 16:09:52');
INSERT INTO `sys_log` VALUES (215, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005007505416870117', '2023-03-30 16:09:57');
INSERT INTO `sys_log` VALUES (216, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0050008296966552734', '2023-03-30 16:09:58');
INSERT INTO `sys_log` VALUES (217, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004004478454589844', '2023-03-30 16:12:05');
INSERT INTO `sys_log` VALUES (218, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004831790924072266', '2023-03-30 16:12:06');
INSERT INTO `sys_log` VALUES (219, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00552058219909668', '2023-03-30 16:12:09');
INSERT INTO `sys_log` VALUES (220, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005094766616821289', '2023-03-30 16:12:15');
INSERT INTO `sys_log` VALUES (221, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.004460811614990234', '2023-03-30 16:12:16');
INSERT INTO `sys_log` VALUES (222, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005595207214355469', '2023-03-30 16:12:18');
INSERT INTO `sys_log` VALUES (223, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00637507438659668', '2023-03-30 16:12:20');
INSERT INTO `sys_log` VALUES (224, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.007135629653930664', '2023-03-30 16:12:21');
INSERT INTO `sys_log` VALUES (225, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005018949508666992', '2023-03-30 16:12:31');
INSERT INTO `sys_log` VALUES (226, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005528450012207031', '2023-03-30 16:12:32');
INSERT INTO `sys_log` VALUES (227, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006203889846801758', '2023-03-30 16:14:08');
INSERT INTO `sys_log` VALUES (228, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005730867385864258', '2023-03-30 16:14:11');
INSERT INTO `sys_log` VALUES (229, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0072345733642578125', '2023-03-30 16:14:35');
INSERT INTO `sys_log` VALUES (230, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006320476531982422', '2023-03-30 16:14:37');
INSERT INTO `sys_log` VALUES (231, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0045392513275146484', '2023-03-30 16:14:49');
INSERT INTO `sys_log` VALUES (232, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006768465042114258', '2023-03-30 16:14:50');
INSERT INTO `sys_log` VALUES (233, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005641937255859375', '2023-03-30 16:15:52');
INSERT INTO `sys_log` VALUES (234, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0059854984283447266', '2023-03-30 16:16:42');
INSERT INTO `sys_log` VALUES (235, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005468845367431641', '2023-03-30 16:16:47');
INSERT INTO `sys_log` VALUES (236, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006947755813598633', '2023-03-30 16:16:48');
INSERT INTO `sys_log` VALUES (237, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005000114440917969', '2023-03-30 16:17:53');
INSERT INTO `sys_log` VALUES (238, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006064653396606445', '2023-03-30 16:18:23');
INSERT INTO `sys_log` VALUES (239, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.00516963005065918', '2023-03-30 16:18:33');
INSERT INTO `sys_log` VALUES (240, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005254030227661133', '2023-03-30 16:18:38');
INSERT INTO `sys_log` VALUES (241, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006009340286254883', '2023-03-30 16:20:12');
INSERT INTO `sys_log` VALUES (242, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.006527900695800781', '2023-03-30 16:20:24');
INSERT INTO `sys_log` VALUES (243, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.0065135955810546875', '2023-03-30 16:20:29');
INSERT INTO `sys_log` VALUES (244, '/api/user/list', 'GET', '127.0.0.1', '{\'page\': \'1\', \'page_size\': \'10\'}', '0.005031108856201172', '2023-03-30 16:20:58');

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
  `is_deleted` smallint NULL DEFAULT 0 COMMENT '是否删除: 0 未删除 1 已删除',
  `create_time` datetime NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'admin', '30780cc6f2e56945aaf9c9578c932e22', NULL, 0, NULL, 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');
INSERT INTO `user` VALUES (2, 'user', '30780cc6f2e56945aaf9c9578c932e22', NULL, 1, NULL, 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');
INSERT INTO `user` VALUES (3, 'guest', '30780cc6f2e56945aaf9c9578c932e22', NULL, 2, NULL, 0, '2023-03-29 02:34:58', '2023-03-29 02:34:58');

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
