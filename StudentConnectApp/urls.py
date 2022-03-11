from django.urls import path
from StudentConnectApp import views

app_name="StudentConnect"

urlpatterns=[
    path('', views.index, name="index"),
    #add more urls here please
]
