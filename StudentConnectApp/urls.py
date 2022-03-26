
from django.urls import path
from StudentConnectApp import views

app_name="StudentConnect"

urlpatterns=[
    path('', views.index, name="index"),
    path('myAccount/', views.MyAccount, name="myAccount"),
    path('Home/', views.Home, name="Home"),
    path('myMatches/', views.MyMatches, name="myMatches"),
    path('findMatches/', views.findMatches, name='findMatches'),
    path('loadingMatches/', views.loadingMatches, name='loadMatches'),
    path('Profile/<username>/', views.otherProfiles, name='otherProfiles'),
    path('Help/', views.Help, name='Help'),
    path('Signup/', views.Signup, name='Signup'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('editMyAccount/', views.editMyAccount, name="editMyAccount"),
    path('forgot_password/', views.forgotPassword, name='forgotPassword'),
]
