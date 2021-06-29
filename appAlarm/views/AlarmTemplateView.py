import json

from datetime import datetime
from appAlarm.forms import AlarmTemplateForm
from appAlarm.manages import template_manage
from django.views.generic import ListView, FormView
from appAlarm.utils import generate_id
from appAlarm.utils import return_result
from django.core.paginator import Paginator

class GetTemplateView(ListView):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        parm = self.request.GET.dict()
        if parm.get("channel_type") is not None:
            data = template_manage.get_template_by_type(parm.get("channel_type"))
            parm["pagesize"] = 1000
            parm["pagenum"] = 1
            print(data)
            if data.get("status"):
                return return_result.http_result(200, data=data.get("data"))
            else:
                return_result.http_result(500, message=data.get("message"))
        else:
            data = template_manage.get_template_by_parm(parm.get("search", " "))
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

class CreateTemplateView(FormView):
    form_class = AlarmTemplateForm
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        form =self.get_form()
        if form.is_valid():
            template_id = generate_id()
            now_time = datetime.now()
            form.cleaned_data["template_id"] = template_id
            form.cleaned_data["create_time"] = now_time
            form.cleaned_data["update_time"] = now_time
            form.cleaned_data["create_user"] = "admin"
            form.cleaned_data["update_user"] = "admin"
            result = template_manage.create_alarm_template(**form.cleaned_data)
        else:
            return return_result.http_result(500, message="创建失败，请检查名称!")
        status = 200 if result.get("status") else 500
        return return_result.http_result(status, message=result.get("message"))

class UpdateTemplateView(FormView):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        # form = self.get_form()
        data = json.loads(self.request.body)
        data["update_time"] = datetime.now()
        data["update_user"] = "admin"
        print(data)
        result = template_manage.update_template(**data)
        status = 200 if result.get("status") else 500
        return return_result.http_result(status, message=result.get("message"))


class DeleteAlarmTemplateByIdView(FormView):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        parm = json.loads(self.request.body)
        template_id = parm.get("template_id", None)
        if template_id is None:
            return return_result.http_result(400, message="缺少参数（）")
        result_delete = template_manage.template_delete(template_id)

        if result_delete.get("status"):
            return return_result.http_result(200, result_delete.get("message"))
        else:
            return return_result.http_result(400, result_delete.get("message"))