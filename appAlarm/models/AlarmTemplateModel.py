import django.utils.timezone as timezone
from django.db import models


class AlarmTemplate(models.Model):
    template_id = models.CharField("模板id", max_length=34, unique=True, primary_key=True)
    template_type = models.CharField("模板类型", max_length=34)
    channel_type = models.CharField("渠道类型", max_length=34)
    template_name = models.CharField("模板名称", max_length=255, unique=True)
    template_content = models.CharField("模板地址", max_length=5000)
    create_time = models.DateTimeField("创建时间", default=timezone.now)
    update_time = models.DateTimeField("更新时间", default=timezone.now)
    create_user = models.CharField("创建人", max_length=255, default="admin")
    update_user = models.CharField("更新人", max_length=255, default="admin")