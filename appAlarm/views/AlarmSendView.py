import json

from django.views import View
from appAlarm.utils import return_result

class AlarmSendView(View):
    http_method_names = ["post"]

    def post(self, request, channel_id, *args, **kwargs):
        print(json.loads(self.request.body))
        print(channel_id)
        return return_result.http_result(200, 'Hello, World!')
