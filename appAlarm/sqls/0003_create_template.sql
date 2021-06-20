-- Create model AlarmTemplate
--

CREATE TABLE `appAlarm_alarmtemplate` (`template_id` varchar(34) NOT NULL PRIMARY KEY, `template_type` varchar(34) NOT NULL, `template_name` varchar(255) NOT NULL UNIQUE, `template_content` varchar(5000) NOT NULL, `create_time` datetime(6) NOT NULL, `update_time` datetime(6) NOT NULL, `create_user` varchar(255) NOT NULL, `update_user` varchar(255) NOT NULL);