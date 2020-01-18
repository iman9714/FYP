from django.contrib import admin
from django.urls import include, path

from .views import (
    event_view,
    event_management,
    create_event,
    view_volunteer_detail,
    recommended_event,
    )


urlpatterns = [
    path('home/', recommended_event, name="home"),
    path('event/', event_view, name="event_view"),
    path('create_event', create_event, name="create_event"),
    path('<id>/detail', event_management, name="detail"),
    path('volunteer-profile/<volunteer_id>', view_volunteer_detail, name="view_volunteer_profile"),

]
