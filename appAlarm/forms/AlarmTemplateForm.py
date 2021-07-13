from appAlarm.models import AlarmTemplate
from django import forms


class AlarmTemplateForm(forms.ModelForm):
    class Meta:
        model = AlarmTemplate
        fields = ["template_type", "channel_type", "template_name", "template_content", "notify_type"]

    def clean_channel_type(self):
        channel_type = self.cleaned_data.get("channel_type")
        if channel_type not in ["dingding", "weixin", "feishu"]:
            self.add_error("channel_type", "模板类型不正确")
        else:
            return channel_type

    def clean_notify_type(self):
        notify_type = self.cleaned_data.get("notify_type")
        if notify_type not in ["text", "markdown"]:
            self.add_error("notify_type", "通知形式不正确")
        else:
            return notify_type

    def clean_template_type(self):
        template_type = self.cleaned_data.get("template_type")
        if template_type not in ["alarm", "restore"]:
            self.add_error("template_type", "模板类型不正确")
        else:
            return template_type