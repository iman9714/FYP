from django.contrib import admin
from django.urls import include, path
from account.views import account_management, account_register, user_logout #account_edit_profile,

urlpatterns = [
    path('logout/',  user_logout, name="user_logout"),
    path('profile/',  account_management, name="profile"),
    path('register/',  account_register, name="register"),
    #path('profile/edit/',  account_edit_profile, name="edit_profile"),
]
