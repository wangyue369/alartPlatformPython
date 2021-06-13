-- Create model NavigationLevelTwoModel
--
CREATE TABLE `appAlarm_navigationleveltwomodel` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `level_one_name` varchar(255) NOT NULL, `level_two_name` varchar(255) NOT NULL UNIQUE, `level_two_type` varchar(255) NOT NULL UNIQUE)
;
--
-- Create model NavigationModel
--
CREATE TABLE `appAlarm_navigationmodel` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `level_one_name` varchar(255) NOT NULL UNIQUE);

--
-- Insert data
--
INSERT INTO `appAlarm_navigationmodel` (`level_one_name`) values ("告警渠道管理");
INSERT INTO `appAlarm_navigationmodel` (`level_one_name`) values ("告警模板管理");
INSERT INTO `appAlarm_navigationmodel` (`level_one_name`) values ("告警历史管理");
INSERT INTO `appAlarm_navigationmodel` (`level_one_name`) values ("权限管理");

INSERT INTO `appAlarm_navigationleveltwomodel` (`level_one_name`, `level_two_name`, `level_two_type`) values ("告警渠道管理","钉钉告警", "dingding");
INSERT INTO `appAlarm_navigationleveltwomodel` (`level_one_name`, `level_two_name`, `level_two_type`) values ("告警渠道管理","企业微信告警", "weixin");
INSERT INTO `appAlarm_navigationleveltwomodel` (`level_one_name`, `level_two_name`, `level_two_type`) values ("告警渠道管理","飞书告警", "feishu");
INSERT INTO `appAlarm_navigationleveltwomodel` (`level_one_name`, `level_two_name`, `level_two_type`) values ("告警模板管理","告警模板", "alarm_template");
INSERT INTO `appAlarm_navigationleveltwomodel` (`level_one_name`, `level_two_name`, `level_two_type`) values ("告警历史管理","告警历史", "alarm_history");
INSERT INTO `appAlarm_navigationleveltwomodel` (`level_one_name`, `level_two_name`, `level_two_type`) values ("告警历史管理","告警分类", "alarm_type");
INSERT INTO `appAlarm_navigationleveltwomodel` (`level_one_name`, `level_two_name`, `level_two_type`) values ("告警历史管理","图表展示", "chart_manager");
INSERT INTO `appAlarm_navigationleveltwomodel` (`level_one_name`, `level_two_name`, `level_two_type`) values ("权限管理","权限管理", "permission_manager");