
from django.views.generic import ListView
from appAlarm.manages import navigation_manage
from appAlarm.utils import return_result
class NavigationGetView(ListView):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        data = navigation_manage.get_all_navigation()
        if data.get("status"):
            return return_result.http_result(data=data.get("data"))
        else:
            return return_result.http_result(500,data.get("message"))
