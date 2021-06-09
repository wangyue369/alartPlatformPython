import json

from datetime import datetime
from appAlarm.forms import AlarmChannelForm
from appAlarm.managers import alarm_channel_manager
from django.views.generic import ListView, FormView
from django.http import HttpResponse
from appAlarm.utils import generate_id

class GetAlarmChannelView(ListView):
    http_method_names = ["get"]
    def get(self, request, *args, **kwargs):
        data = alarm_channel_manager.get_alarm_channel_all()
        return HttpResponse(json.loads(data))


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
            alarm_channel_manager.create_alarm_channel(**form.cleaned_data)
        else:
            return HttpResponse(form.errors.as_json())
        return HttpResponse("aaaa")

