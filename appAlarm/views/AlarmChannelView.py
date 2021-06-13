import json

from datetime import datetime
from appAlarm.forms import AlarmChannelForm
from appAlarm.manages import alarm_channel_manage
from django.views.generic import ListView, FormView
from django.http import HttpResponse
from appAlarm.utils import generate_id
from appAlarm.utils import return_result, ReturnResultUtil
from django.core.paginator import Paginator


class GetAlarmChannelView(ListView):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        parm = self.request.GET.dict()
        if len(parm) == 0:
            return return_result.http_result(400, message="缺少参数，请检查请求参数！")

        data = alarm_channel_manage.get_alarm_channel_by_parm(parm.get("channel_type"), parm.get("search", " "))
        if data.get("status"):
            paginator = Paginator(data.get("data"), parm.get("pagesize", 10))
            page_obj = paginator.get_page(parm.get("pagenum", 1))
            total = paginator.count
            result = {
                "total": total,
                "data": page_obj.object_list
            }
            return return_result.http_result(200, data=result)
        else:
            return return_result.http_result(500, message=data.get("message"))


class CreateAlarmView(FormView):
    form_class = AlarmChannelForm
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        print(111)
        if form.is_valid():
            print(222)
            channel_id = "c-" + generate_id()
            now_time = datetime.now()
            form.cleaned_data["channel_id"] = channel_id
            form.cleaned_data["create_time"] = now_time
            form.cleaned_data["update_time"] = now_time
            form.cleaned_data["create_user"] = "admin"
            form.cleaned_data["update_user"] = "admin"
            result = alarm_channel_manage.create_alarm_channel(**form.cleaned_data)
        else:
            return return_result.http_result(500, message="创建失败，请检查名称、地址是否重复！")
        status = 200 if result.get("status") else 500
        return return_result.http_result(status, message=result.get("message"))


class UpdateAlarmView(FormView):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        # form = self.get_form()
        data = json.loads(self.request.body)
        data["update_time"] = datetime.now()
        data["update_user"] = "admin"
        result = alarm_channel_manage.channel_update(**data)
        status = 200 if result.get("status") else 500
        return return_result.http_result(status, message=result.get("message"))


class DeleteAlarmChannelByIdView(FormView):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        parm = json.loads(self.request.body)
        channel_id = parm.get("channel_id", None)
        if channel_id is None:
            return return_result.http_result(400, message="缺少参数（）")
        result_delete = alarm_channel_manage.channel_delete(channel_id)

        if result_delete.get("status"):
            return return_result.http_result(200, result_delete.get("message"))
        else:
            return return_result.http_result(400, result_delete.get("message"))
