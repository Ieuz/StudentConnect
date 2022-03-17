from django.urls import path
from StudentConnectApp import views

app_name="StudentConnect"

urlpatterns=[
    path('', views.index, name="index"),
    path('myAccount/', views.MyAccount, name="myAccount"),
    path('Home/', views.Home, name="Home"),
    path('myMatches/', views.MyMatches, name="myMatches"),
    path('Login/', views.Login, name='Login'),
    path('Help/', views.Help, name='Help'),
    path('Signup/', views.Signup, name='Signup'),
    #add more urls here please
]
