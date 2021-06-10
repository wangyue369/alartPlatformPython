import json
from datetime import datetime
from appAlarm.models import AlarmChannel
from django.core import serializers
from django.db.models import Q
from appAlarm.utils import return_result


class AlarmChannelManage:
    def create_alarm_channel(self, channel_id:str, channel_type:str, channel_name:str, channel_access:str,
                             create_time:datetime=None, update_time:datetime=None, create_user:str="admin",
                             update_user:str="admin", is_active: bool = True):

        if self.channel_name_or_access_exist(channel_name, channel_access):
            print("name or access repeat")
            return return_result.result(False, message="name or access repeat！")
        try:
            print(is_active)
            AlarmChannel.objects.create(channel_id=channel_id, channel_type=channel_type, channel_name=channel_name,
                                    channel_access=channel_access, create_time=create_time, update_time=update_time,
                                    create_user=create_user, update_user=update_user, is_active= is_active)
            return return_result.result(True, message="创建成功！")
        except Exception as e:
            return return_result.result(True, message="创建失败！")

    def get_alarm_channel_all(self):
        all_alarm_channels = serializers.serialize("json", AlarmChannel.objects.all())
        return all_alarm_channels

    def get_alarm_channel_by_type(self, channel_type:str):
        try:
            all_alarm_channels = list(AlarmChannel.objects.filter(channel_type=channel_type).order_by("update_time").reverse().values())
            total = len(all_alarm_channels)
            print(serializers.serialize("json",AlarmChannel.objects.filter(channel_type=channel_type).order_by("update_time")))
            result = {"total": total, "data": all_alarm_channels}
        except Exception as e:
            return return_result.result(False, message="获取该告警类型失败！")
        return return_result.result(True,data=result)

    def channel_name_or_access_exist(self, channel_name:str, channel_access:str, channel_id:str = None,):
        if channel_id == None:
            return AlarmChannel.objects.filter(Q(channel_name=channel_name) | Q(channel_access=channel_access)).exists()
        else:
            return AlarmChannel.objects.filter(~Q(channel_id=channel_id) & (Q(channel_name=channel_name) | Q(channel_access=channel_access))).exists()

    def channel_id_exist(self, channel_id:str):
        return AlarmChannel.objects.filter(channel_id=channel_id).values() != 0

    def channel_update(self, channel_id:str, channel_name:str, channel_access:str,
                       is_active: bool = True, update_time:datetime=None, update_user:str="admin"):
        if not self.channel_id_exist(channel_id):
            return return_result.result(False, message="无此记录！")
        if self.channel_name_or_access_exist(channel_id=channel_id, channel_name=channel_name,
                                                 channel_access=channel_access):
            return return_result.result(False, message="渠道名称或渠道地址重复！")
        try:
            AlarmChannel.objects.filter(channel_id=channel_id).update(
                                    channel_access=channel_access, channel_name=channel_name,
                                    is_active=is_active, update_user=update_user, update_time=update_time)
            return return_result.result(True, message="修改成功！")
        except Exception as e:
            print(e)
            return return_result.result(False, message="修改失败！")




