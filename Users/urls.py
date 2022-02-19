from django.urls import path, include
from .views import *

urlpatterns = [
    path("user-list", UserListView.as_view(), name="user-list"),
    path("user-create", UserCreateView.as_view(), name="user-create"),
    path("user-update/<int:pk>/", UserUpdateView.as_view(), name="user-update"),
    path("user-delete/<int:pk>/", UserDeleteView.as_view(), name="user-delete"),
]
