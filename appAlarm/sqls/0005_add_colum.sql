--
-- Remove field template_name from alarmchannel
--
ALTER TABLE `appAlarm_alarmchannel` DROP COLUMN `template_name`;
--
-- Add field alarm_template_name to alarmchannel
--
ALTER TABLE `appAlarm_alarmchannel` ADD COLUMN `alarm_template_name` varchar(255)  NOT NULL;
ALTER TABLE `appAlarm_alarmchannel` ALTER COLUMN `alarm_template_name` DROP DEFAULT;
--
-- Add field restore_template_name to alarmchannel
--
ALTER TABLE `appAlarm_alarmchannel` ADD COLUMN `restore_template_name` varchar(255)  NOT NULL;
ALTER TABLE `appAlarm_alarmchannel` ALTER COLUMN `restore_template_name` DROP DEFAULT;
--
-- Add field channel_type to alarmtemplate
--
ALTER TABLE `appAlarm_alarmtemplate` ADD COLUMN `channel_type` varchar(34)  NOT NULL;
ALTER TABLE `appAlarm_alarmtemplate` ALTER COLUMN `channel_type` DROP DEFAULT;
--
-- Alter field template_content on alarmtemplate
--
--
-- Alter field template_id on alarmtemplate
--
--
-- Alter field template_name on alarmtemplate
--
--
-- Alter field template_type on alarmtemplate
--
