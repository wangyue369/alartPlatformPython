from django.db import models

class NavigationModel(models.Model):
    level_one_name = models.CharField("一级标题名称", max_length=255, unique=True)

class NavigationLevelTwoModel(models.Model):
    level_one_name = models.CharField("一级标题名称", max_length=255)
    level_two_name = models.CharField("二级标题名称", max_length=255, unique=True)
    level_two_type = models.CharField("二级标题类型", max_length=255, unique=True)
