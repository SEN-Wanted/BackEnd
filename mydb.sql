/*
 Navicat MySQL Data Transfer

 Source Server         : 1
 Source Server Type    : MySQL
 Source Server Version : 50720
 Source Host           : localhost:3306
 Source Schema         : mydb

 Target Server Type    : MySQL
 Target Server Version : 50720
 File Encoding         : 65001

 Date: 26/06/2018 18:58:41
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for comments
-- ----------------------------
-- DROP TABLE IF EXISTS `comments`;
-- CREATE TABLE `comments`  (
--   `id` int(11) NOT NULL AUTO_INCREMENT,
--   `username` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
--   `storeId` int(11) NOT NULL,
--   `content` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
--   `rating` smallint(6) NOT NULL,
--   PRIMARY KEY (`id`) USING BTREE,
--   INDEX `username`(`username`) USING BTREE,
--   INDEX `storeId`(`storeId`) USING BTREE,
--   CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
--   CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`storeId`) REFERENCES `stores` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
-- ) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for coupons
-- ----------------------------
-- DROP TABLE IF EXISTS `coupons`;
-- CREATE TABLE `coupons`  (
--   `id` int(11) NOT NULL AUTO_INCREMENT,
--   `discount` smallint(6) NOT NULL,
--   `condition` smallint(6) NOT NULL,
--   `username` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
--   `expiredTime` date NOT NULL,
--   `status` tinyint(1) NOT NULL,
--   PRIMARY KEY (`id`) USING BTREE,
--   INDEX `username`(`username`) USING BTREE,
--   CONSTRAINT `coupons_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
-- ) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for dishes
-- ----------------------------
DROP TABLE IF EXISTS `dishes`;
CREATE TABLE `dishes`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dishName` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `dishPrice` float NOT NULL,
  `monthlySale` int(11) NOT NULL,
  `storeId` int(11) NOT NULL,
  `img` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `title` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `storeId`(`storeId`) USING BTREE,
  CONSTRAINT `dishes_ibfk_1` FOREIGN KEY (`storeId`) REFERENCES `stores` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of dishes
-- ----------------------------
INSERT INTO `dishes` VALUES (1, '经典麦辣鸡腿堡', 30, 400, 1, '麦辣鸡腿堡.jpg', '主食');
INSERT INTO `dishes` VALUES (2, '果木烟熏风味那么大鸡翅', 30, 300, 1, '果木烟熏风味那么大鸡翅', '小食');
INSERT INTO `dishes` VALUES (3, '超级芒果绵绵冰', 30, 300, 2, '超级芒果绵绵冰', '超级芒果绵绵冰系列');
INSERT INTO `dishes` VALUES (4, '芒果牛奶冰', 20, 250, 2, '芒果牛奶冰', '杨小杯');
INSERT INTO `dishes` VALUES (5, '奶茶烧仙草', 15, 300, 2, '奶茶烧仙草', '纯手工烧仙草');
INSERT INTO `dishes` VALUES (6, '热餐三明治', 40, 500, 3, '9ef2976629c64b2864a2909caf79a18362399', '玩转新吃法');
INSERT INTO `dishes` VALUES (7, '火腿三明治', 30, 500, 3, '241235a28410d7b2fc231ec2ac71fb60662907', '低脂三明治');

-- ----------------------------
-- Table structure for favorites
-- ----------------------------
-- DROP TABLE IF EXISTS `favorites`;
-- CREATE TABLE `favorites`  (
--   `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
--   `username` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
--   `storeId` int(11) NOT NULL,
--   PRIMARY KEY (`id`) USING BTREE,
--   INDEX `username`(`username`) USING BTREE,
--   INDEX `storeId`(`storeId`) USING BTREE,
--   CONSTRAINT `favorites_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
--   CONSTRAINT `favorites_ibfk_2` FOREIGN KEY (`storeId`) REFERENCES `stores` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
-- ) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for food_list
-- ----------------------------
DROP TABLE IF EXISTS `food_list`;
CREATE TABLE `food_list`  (
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `dishName` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `number` int(11) NOT NULL,
  `price` float NOT NULL,
  `orderID` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `orderID`(`orderID`) USING BTREE,
  CONSTRAINT `food_list_ibfk_1` FOREIGN KEY (`orderID`) REFERENCES `orders` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of food_list
-- ----------------------------
INSERT INTO `food_list` VALUES (1, '麦辣鸡腿堡', 1, 1, 1);
INSERT INTO `food_list` VALUES (2, '那么大鸡翅', 1, 1, 1);
INSERT INTO `food_list` VALUES (3, '芒果牛奶冰', 1, 1, 2);

-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders`  (
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `storeName` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `createTime` datetime(0) NOT NULL,
  -- `status` tinyint(1) NOT NULL,
  -- `couponId` int(11) NULL DEFAULT NULL,
  `mealFee` float NOT NULL,
  `ServiceFee` float NOT NULL,
  `payPrice` float NOT NULL,
  `totalPrice` float NOT NULL,
  `paymengtMethod` int(11) NOT NULL,
  `rating` float NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `username`(`username`) USING BTREE,
  -- INDEX `couponId`(`couponId`) USING BTREE,
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
  -- CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`couponId`) REFERENCES `coupons` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of orders
-- ----------------------------
-- INSERT INTO `orders` VALUES (1, '13719335341', '麦当劳', '2018-06-26 18:45:26', 1, 1, 1, 1, 1, 1);
-- INSERT INTO `orders` VALUES (2, '13719335341', '杨小贤', '2018-06-26 18:50:31', 1, 1, 1, 1, 1, 1);

-- ----------------------------
-- Table structure for recommendation
-- ----------------------------
-- DROP TABLE IF EXISTS `recommendation`;
-- CREATE TABLE `recommendation`  (
--   `storeId` int(11) NOT NULL,
--   PRIMARY KEY (`storeId`) USING BTREE,
--   CONSTRAINT `recommendation_ibfk_1` FOREIGN KEY (`storeId`) REFERENCES `stores` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
-- ) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stores
-- ----------------------------
DROP TABLE IF EXISTS `stores`;
CREATE TABLE `stores`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storeName` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `distance` float NOT NULL,
  `monthlySale` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `price` float NOT NULL,
  `isDiscount` tinyint(1) NULL DEFAULT NULL,
  `discountNumber` float NULL DEFAULT NULL,
  `description` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `rating` float NULL DEFAULT NULL,
  `ratingNum` smallint(6) NULL DEFAULT NULL,
  `isAppOffer` tinyint(1) NULL DEFAULT NULL,
  `title` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `img` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `storeName`(`storeName`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of stores
-- ----------------------------
INSERT INTO `stores` VALUES (1, '麦当劳', 0.1, '1000', 40, 1, 20, '汉堡', 4.4, 600, 1, '品牌餐饮', '麦当劳LOGO');
INSERT INTO `stores` VALUES (2, '杨小贤', 0.2, '2000', 30, 0, 30, '绵绵冰', 4.5, 400, 0, '甜品', '杨小贤');
INSERT INTO `stores` VALUES (3, '赛百味', 0.3, '3000', 50, 1, 10, '三明治', 4.4, 500, 1, '西餐', 'logo');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `nickname` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password_hash` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `payPassword` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `money` float NOT NULL,
  `description` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `isAdmin` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('13719335341', '111', '123456', '123456', 0, 'lll', 0);
INSERT INTO `users` VALUES ('13719335349', '222', '123456', '123456', 0, '111', 1);

SET FOREIGN_KEY_CHECKS = 1;
