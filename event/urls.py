from django.contrib import admin
from django.urls import include, path

from .views import (
    event_view,
    event_detail,
    create_event,
    view_volunteer_detail,
    )


urlpatterns = [
    path('event/', event_view, name="event_view"),
    path('create_event', create_event, name="create_event"),
    path('<id>/detail', event_detail, name="detail"),
    path('volunteer-profile/<volunteer_id>', view_volunteer_detail, name="view_volunteer_profile"),

]
