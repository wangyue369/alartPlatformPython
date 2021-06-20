--
-- Create model AlarmChannel
--
CREATE TABLE `appAlarm_alarmchannel` (`channel_id` varchar(34) NOT NULL PRIMARY KEY, `channel_type` varchar(34) NOT NULL, `channel_name` varchar(255) NOT NULL UNIQUE, `channel_access` varchar(1000) NOT NULL UNIQUE, `channel_webhook`
 varchar(255) NOT NULL UNIQUE, `is_active` bool NOT NULL, `create_time` datetime(6) NOT NULL, `update_time` datetime(6) NOT NULL, `create_user` varchar(255) NOT NULL, `update_user` varchar(255) NOT NULL);
--
