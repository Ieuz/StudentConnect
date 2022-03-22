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
    path('Profile/', views.Profile, name='Profile'),
    #add more urls here please
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    path('editMyAccount/', views.editMyAccount, name="editMyAccount"),
]
