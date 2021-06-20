from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('alarmChannel/get.json', views.GetAlarmChannelView.as_view()),
    path('alarmChannel/create.json', views.CreateAlarmView.as_view()),
    path('alarmChannel/update.json', views.UpdateAlarmView.as_view()),
    path('alarmChannel/delete.json', views.DeleteAlarmChannelByIdView.as_view()),
    path('navigation/get.json', views.NavigationGetView.as_view()),

    # path(r'<str:env>/alarm.json', views.AlarmSendView.as_view()),
    re_path('(?P<channel_id>[0-9a-z]{32})/alarm.json', views.AlarmSendView.as_view()),

    # template

    path('alarmTemplate/get.json', views.GetTemplateView.as_view()),
    path('alarmTemplate/create.json', views.CreateAlarmView.as_view()),
    path('alarmTemplate/update.json', views.UpdateTemplateView.as_view()),
    path('alarmTemplate/delete.json', views.DeleteAlarmTemplateByIdView.as_view()),
]
