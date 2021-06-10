import json

from datetime import datetime
from appAlarm.forms import AlarmChannelForm, AlarmChannelUpdateForm
from appAlarm.manages import alarm_channel_manage
from django.views.generic import ListView, FormView
from django.http import HttpResponse
from appAlarm.utils import generate_id
from appAlarm.utils import return_result

class GetAlarmChannelView(ListView):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        parm = self.request.GET.dict()
        if len(parm) == 0:
            return return_result.http_result(400, message="缺少参数，请检查请求参数！")
        data = alarm_channel_manage.get_alarm_channel_by_type(parm.get("channel_type"))
        print(data)
        print(11111)
        if data.get("status"):
            return return_result.http_result(200, data=data.get("data"))
        else:
            return return_result.http_result(500, message=data.get("message"))


class CreateAlarmView(FormView):
    form_class = AlarmChannelForm
    http_method_names = ["post"]
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            channel_id = "c-" + generate_id()
            now_time = datetime.now()
            form.cleaned_data["channel_id"] = channel_id
            form.cleaned_data["create_time"] = now_time
            form.cleaned_data["update_time"] = now_time
            form.cleaned_data["create_user"] = "admin"
            form.cleaned_data["update_user"] = "admin"
            print(form.cleaned_data)
            result = alarm_channel_manage.create_alarm_channel(**form.cleaned_data)
        else:
            return return_result.http_result(500, message=form.errors.as_json())
        status = 200 if result.get("status") else 500
        return return_result.http_result(status, message=result.get("message"))

class UpdateAlarmView(FormView):
    # form_class = AlarmChannelUpdateForm
    http_method_names = ["post"]
    def post(self, request, *args, **kwargs):
        # form = self.get_form()
        data = json.loads(self.request.body)
        data["update_time"] = datetime.now()
        data["update_user"] = "admin"
        result = alarm_channel_manage.channel_update(**data)
        status = 200 if result.get("status") else 500
        return return_result.http_result(status, message=result.get("message"))
        # if form.is_valid():
        #     now_time = datetime.now()
        #     form.cleaned_data["update_time"] = now_time
        #     form.cleaned_data["update_user"] = "admin"
        #     print(form.cleaned_data)
        #     result = alarm_channel_manage.channel_update(**form.cleaned_data)
        # else:
        #     print(1111)
        #     return return_result.http_result(500, message=form.errors.as_json())
        # status = 200 if result.get("status") else 500
        # return return_result.http_result(status, message=result.get("message"))

