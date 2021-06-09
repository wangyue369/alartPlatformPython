from appAlarm.models import AlarmChannel
from django import forms

class AlarmChannelForm(forms.ModelForm):
    class Meta:
        model = AlarmChannel
        fields = ["channel_type", "channel_name", "channel_access"]

    def clean_channel_type(self):
        channel_type = self.cleaned_data.get("channel_type")
        if channel_type not in ["dingding_webhook", "weixin_webhook", "feishu_webhook"]:
            self.add_error("channel_type","渠道类型不正确")
        else:
            return channel_type