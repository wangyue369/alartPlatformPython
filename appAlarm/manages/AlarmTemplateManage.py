import logging

from datetime import datetime
from appAlarm.models import AlarmTemplate
from django.core import serializers
from appAlarm.utils import return_result

logger = logging.getLogger('django')


class AlarmTemplateManage:
    def get_template_all(self):
        all_template = serializers.serialize("json", AlarmTemplate.objects.all())
        return return_result.result(True, data=all_template)

    def get_template_by_parm(self, template_name: str = " "):
        try:
            if len(template_name) == 0:
                all_alarm_templates = list(
                    AlarmTemplate.objects.all().order_by("update_time").reverse().values())
            else:
                all_alarm_templates = list(AlarmTemplate.objects.filter(template_name__contains=template_name).order_by(
                    "update_time").reverse().values())
        except Exception as e:
            logger.error("get message failure: {ex}".format(ex=e))
            return return_result.result(False, message="获取数据失败！")
        return return_result.result(True, data=all_alarm_templates)

    def get_template_by_type(self, channel_type: str = " "):
        try:
            all_alarm_templates = list(AlarmTemplate.objects.filter(channel_type=channel_type, template_type="alarm").order_by(
                    "update_time").reverse().values())
            all_restore_templates = list(
                AlarmTemplate.objects.filter(channel_type=channel_type, template_type="restore").order_by(
                    "update_time").reverse().values())
            data = {
                "alarm": all_alarm_templates,
                "restore": all_restore_templates
            }
        except Exception as e:
            logger.error("get message failure: {ex}".format(ex=e))
            return return_result.result(False, message="获取数据失败！")
        return return_result.result(True, data=data)

    def create_alarm_template(self, template_id: str, template_name: str, template_type: str, channel_type:str, template_content: str, notify_type:str,
                              create_time: datetime = None, update_time: datetime = None, create_user: str = "admin",
                              update_user: str = "admin"):
        if self.template_name_exist(template_name):
            logger.error("template_name exist: {name}".format(name=template_name))
            return return_result.result(False, message="template_name exist!")
        try:
            AlarmTemplate.objects.create(template_id=template_id, template_name=template_name,channel_type=channel_type,
                                         template_type=template_type, template_content=template_content,
                                         create_time=create_time, update_time=update_time, create_user=create_user,
                                         update_user=update_user, notify_type=notify_type)
            return return_result.result(True, message="创建成功！")
        except Exception as e:
            logging.error("create template failure: {ex}".format(ex=e))
            return return_result.result(True, message="创建失败！")

    def template_name_exist(self, name):
        return AlarmTemplate.objects.filter(template_name=name).exists()

    def template_id_exist(self, template_id: str):
        return AlarmTemplate.objects.filter(template_id=template_id).values() != 0

    def update_template(self, template_id: str, template_name: str, template_content: str, notify_type:str, update_time: datetime = None,
                        update_user: str = "admin"):
        if not self.template_id_exist(template_id):
            return return_result.result(False, message="无此记录！")

        # if self.template_name_exist(template_name):
        #     return return_result.result(False, message="模板名称重复！")

        try:
            AlarmTemplate.objects.filter(template_id=template_id).update(
                template_name=template_name, template_content=template_content,
                update_user=update_user, update_time=update_time, notify_type=notify_type
            )
            return return_result.result(True, message="修改成功！")
        except Exception as e:
            logger.error("update failure: {ex}".format(ex=e))
            return return_result.result(False, message="修改失败！")

    def template_delete(self, template_id: str):
        if not self.template_id_exist(template_id):
            return return_result.result(False, message="无此id！")

        try:
            AlarmTemplate.objects.filter(template_id=template_id).delete()
        except Exception as e:
            logger.error("delete failure: {ex}".format(ex=e))
            return return_result.result(False, message="删除失败！")

        return return_result.result(True, message="删除成功！")

    def get_template_by_name(self, template_name: str):
        try:
            template_content = AlarmTemplate.objects.filter(template_name=template_name).values("template_content")[0]["template_content"]
        except Exception as e:
            logger.error("get message failure: {ex}".format(ex=e))
            return return_result.result(False, message="获取数据失败！")
        return return_result.result(True, data=template_content)
