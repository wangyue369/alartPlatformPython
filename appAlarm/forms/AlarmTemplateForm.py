from appAlarm.models import AlarmTemplate
from django import forms


class AlarmTemplateForm(forms.ModelForm):
    class Meta:
        model = AlarmTemplate
        fields = ["template_type", "template_name", "template_content"]

    # def clean_template_type(self):assa
    #     template_type = self.cleaned_data.get("template_type")
    #     if template_type not in ["dingding", "weixin", "feishu"]:
    #         self.add_error("template_type", "模板类型不正确")
    #     else:
    #         return template_type
