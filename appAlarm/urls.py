from django.urls import path
from . import views

urlpatterns = [
    path('alarmChannel/get.json', views.AlarmChannelView.GetAlarmChannelView.as_view()),
    path('alarmChannel/create.json', views.AlarmChannelView.CreateAlarmView.as_view())
]