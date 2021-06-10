from appAlarm.models import AlarmChannel
from django import forms

class AlarmChannelUpdateForm(forms.Form):
    # class Meta:
    #     model = AlarmChannel
    #     fields = ["channel_id", "channel_name", "channel_access", "is_active"]

    channel_id = forms.CharField(max_length="34", error_messages={"min_length":'标题字符段不符合要求！'})
    channel_name = forms.CharField(max_length="255", error_messages={"min_length":'标题字符段不符合要求！'})
    channel_access = forms.CharField(max_length="255", error_messages={"min_length":'标题字符段不符合要求！'})
    is_active = forms.BooleanField()

