import logging

from datetime import datetime
from appAlarm.models import AlarmChannel
from django.core import serializers
from django.db.models import Q
from appAlarm.utils import return_result

logger = logging.getLogger('django')


class AlarmChannelManage:
    def create_alarm_channel(self, channel_id: str, channel_type: str, channel_name: str, channel_access: str, channel_webhook, template_name:str,
                             create_time: datetime = None, update_time: datetime = None, create_user: str = "admin",
                             update_user: str = "admin", is_active: bool = True):

        if self.channel_name_or_access_exist(channel_name, channel_access):
            logger.error(
                "name or access repeat! name: {name}, access：{access}".format(name=channel_name, access=channel_access))
            return return_result.result(False, message="name or access repeat！")
        try:
            AlarmChannel.objects.create(channel_id=channel_id, channel_type=channel_type, channel_name=channel_name, template_name=template_name,
                                        channel_access=channel_access, channel_webhook=channel_webhook,create_time=create_time, update_time=update_time,
                                        create_user=create_user, update_user=update_user, is_active=is_active)
            return return_result.result(True, message="创建成功！")
        except Exception as e:
            logger.error(
                "create failure: {ex}".format(ex=e))
            return return_result.result(True, message="创建失败！")

    def get_alarm_channel_all(self):
        all_alarm_channels = serializers.serialize("json", AlarmChannel.objects.all())
        return all_alarm_channels

    def get_alarm_channel_by_parm(self, channel_type: str, channel_name: str = " "):
        try:
            if len(channel_name) == 0:
                all_alarm_channels = list(
                    AlarmChannel.objects.filter(channel_type=channel_type).order_by("update_time").reverse().values())
            else:
                all_alarm_channels = list(AlarmChannel.objects.filter(channel_name__contains=channel_name,
                                                                      channel_type=channel_type).order_by(
                    "update_time").reverse().values())
        except Exception as e:
            logger.error("get message failure: {ex}".format(ex=e))
            return return_result.result(False, message="获取该告警类型失败！")
        return return_result.result(True, data=all_alarm_channels)

    def channel_name_or_access_exist(self, channel_name: str, channel_access: str, channel_id: str = None, ):
        if channel_id == None:
            return AlarmChannel.objects.filter(Q(channel_name=channel_name) | Q(channel_access=channel_access)).exists()
        else:
            return AlarmChannel.objects.filter(
                ~Q(channel_id=channel_id) & (Q(channel_name=channel_name) | Q(channel_access=channel_access))).exists()

    def channel_id_exist(self, channel_id: str):
        return AlarmChannel.objects.filter(channel_id=channel_id).values() != 0

    def channel_update(self, channel_id: str, channel_name: str, channel_access: str, template_name: str,
                       is_active: bool = True, update_time: datetime = None, update_user: str = "admin"):
        if not self.channel_id_exist(channel_id):
            return return_result.result(False, message="无此记录！")
        if self.channel_name_or_access_exist(channel_id=channel_id, channel_name=channel_name,
                                             channel_access=channel_access):
            return return_result.result(False, message="渠道名称或渠道地址重复！")
        try:
            AlarmChannel.objects.filter(channel_id=channel_id).update(
                channel_access=channel_access, channel_name=channel_name, template_name = template_name,
                is_active=is_active, update_user=update_user, update_time=update_time)
            return return_result.result(True, message="修改成功！")
        except Exception as e:
            logger.error("update failure: {ex}".format(ex=e))
            return return_result.result(False, message="修改失败！")

    def channel_delete(self, channel_id: str):
        if not self.channel_id_exist(channel_id):
            return return_result.result(False, message="无此id！")

        try:
            AlarmChannel.objects.filter(channel_id=channel_id).delete()
        except Exception as e:
            logger.error("delete failure: {ex}".format(ex=e))
            return return_result.result(False, message="删除失败！")

        return return_result.result(True, message="删除成功！")
