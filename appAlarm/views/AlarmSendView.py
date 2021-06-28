import json
import jinja2
import requests
from django.views import View
from appAlarm.utils import return_result
from appAlarm.manages import alarm_channel_manage, template_manage

class AlarmSendView(View):
    http_method_names = ["post"]

    def post(self, request, channel_id, *args, **kwargs):
        template_name_result = alarm_channel_manage.get_alarm_channel_by_id(channel_id)
        if not template_name_result.get("status"):
            return return_result.http_result(404, message="无此记录")
        template_name = template_name_result.get("data")["template_name"]
        channel_access = template_name_result.get("data")["channel_access"]
        print(template_name)
        print(channel_access)

        template_content_result = template_manage.get_template_by_name(template_name)

        if not template_content_result.get("status"):
            return return_result.http_result(404, message="无此记录")
        template_content = template_content_result.get("data")

        # print(template_content)

        for alert in json.loads(self.request.body).get("alerts"):
            data = jinja2.Template(source=template_content).render(alert=alert)
            print(json.loads(data))
            print(type(data))
        # data = """### <font color="info">[告警恢复]：a</font> \n
        # ### <font color="info">[告警等级]：a</font> \n
        # ### <font color="info">[告警名称]：a</font> \n
        # ### <font color="info">[告警实例]：a</font> \n
        # ### <font color="info">[告警主机]：a {hostIp}</font> \n
        # ### <font color="info">[告警描述]：a</font> \n
        # ### <font color="info">[开始时间]：a</font> \n
        # ### <font color="info">[恢复时间]：a</font> \n"""
        print(data)
        json_data = {"msgtype": "markdown","markdown":{"content": data}}
        result = requests.post(channel_access, json_data)
        print(result.text)
        return return_result.http_result(200, 'Hello, World!')
