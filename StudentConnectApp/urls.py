from django.urls import path
from StudentConnectApp import views

app_name="StudentConnect"

urlpatterns=[
    path('', views.index, name="index"),
    path('myAccount/', views.MyAccount, name="myAccount"),
    path('Home/', views.Home, name="Home"),
    path('myMatches/', views.MyMatches, name="myMatches"),
    path('Login/', views.Login, name='Login'),
    #add more urls here please
]
