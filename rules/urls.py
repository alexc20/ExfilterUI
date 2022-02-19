from django.urls import path, include
from .views import *

urlpatterns = [
    path("", rules_view, name="rules_view"),
]
