from django.urls import include, path
from . import views

app_name = "event"

urlpatterns = [
    path('', views.event_view, name="eventlist"),
]
