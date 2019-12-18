from django.contrib import admin
from django.urls import include, path
from account.views import account_view_profile, account_register, account_edit_profile

urlpatterns = [
    path('profile/',  account_view_profile, name="profile"),
    path('register/',  account_register, name="register"),
    path('profile/edit/',  account_edit_profile, name="edit_profile"),
]
