from datetime import datetime
from appAlarm.models import AlarmChannel
from django.core import serializers
from django.db.models import Q


class AlarmChannelManager:
    def create_alarm_channel(self, channel_id:str, channel_type:str, channel_name:str, channel_access:str,
                             create_time:datetime=None, update_time:datetime=None, create_user:str="admin",
                             update_user:str="admin"):

        if self.channel_name_or_access_exist(channel_name, channel_access):
            print("name or access repeat")
            return False
        try:
            AlarmChannel.objects.create(channel_id=channel_id, channel_type=channel_type, channel_name=channel_name,
                                    channel_access=channel_access, create_time=create_time, update_time=update_time,
                                    create_user=create_user, update_user=update_user)
            return True
        except Exception as e:
            return False

    def get_alarm_channel_all(self):
        all_alarm_channels = serializers.serialize("json", AlarmChannel.objects.all())
        return all_alarm_channels

    def channel_name_or_access_exist(self, channel_name:str, channel_access:str):
        # AlarmChannel.objects.filter(Q(channel_name=channel_name) | Q(channel_access=channel_access))
        # q = Q()
        # q.connector = "or"
        # q.children.append("channel_name", channel_name)
        # q.children.append("channel_access", channel_access)
        return  AlarmChannel.objects.filter(Q(channel_name=channel_name) | Q(channel_access=channel_access))


