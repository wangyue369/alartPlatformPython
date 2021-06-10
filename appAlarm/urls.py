from django.urls import path
from . import views

urlpatterns = [
    path('alarmChannel/get.json', views.GetAlarmChannelView.as_view()),
    path('alarmChannel/create.json', views.CreateAlarmView.as_view()),
    path('alarmChannel/update.json', views.UpdateAlarmView.as_view()),
    path('navigation/get.json', views.NavigationGetView.as_view())
]