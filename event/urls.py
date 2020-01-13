from django.contrib import admin
from django.urls import include, path

from .views import (
    event_view,
    event_detail,
    create_event,
    )


urlpatterns = [
    path('event/', event_view, name="event_view"),
    path('create_event', create_event, name="create_event"),
    path('<id>/detail', event_detail, name="detail"),
]
