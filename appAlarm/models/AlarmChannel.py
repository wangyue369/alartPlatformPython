import django.utils.timezone as timezone
from django.db import models

class AlarmChannel(models.Model):
    channel_id = models.CharField("渠道id",max_length=34, unique=True, primary_key=True)
    channel_type = models.CharField("渠道类型", max_length=34)
    channel_name = models.CharField("渠道名称", max_length=255, unique=True)
    channel_access = models.CharField("渠道地址", max_length=1000, unique=True)
    create_time = models.DateTimeField("创建时间", default=timezone.now)
    update_time = models.DateTimeField("更新时间", default=timezone.now)
    create_user = models.CharField("创建人", max_length=255, default="admin")
    update_user = models.CharField("更新人", max_length=255, default="admin")
