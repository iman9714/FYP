from django.urls import path
from .views import HomePageView,LoginPageView

urlpatterns = [
    path('login/',LoginPageView.as_view(), name='login'),
    path('',HomePageView.as_view(), name='home'),
]
