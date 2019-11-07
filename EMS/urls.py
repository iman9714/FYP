from django.urls import path
from .views import HomePageView,LoginPageView

urlpatterns = [
    path('login/',LoginPageView.as_view(), name='login'),
    path('home/',HomePageView.as_view(), name='home'),
]
