import json

from appAlarm.utils import return_result
from appAlarm.models import NavigationModel, NavigationLevelTwoModel
from django.core import serializers


class NavigationManage:

    def get_all_navigation(self):
        try:
            all_data = json.loads(serializers.serialize("json", NavigationModel.objects.all().order_by("id")))

            data = []
            for i in all_data:
                tmp_dict = {}
                level_two_data = json.loads(serializers.serialize("json",
                                                                  NavigationLevelTwoModel.objects.filter(level_one_name=i["fields"][
                                                                      "level_one_name"]).order_by("id")))
                tmp_dict["pk"] = i["pk"]
                tmp_dict["name"] = i["fields"]["level_one_name"]
                tmp_dict["childs"] = level_two_data
                data.append(tmp_dict)
        except Exception as e:
            print(e)
            return return_result.result(False, message="查询结果失败")
        return return_result.result(True, data = data)
