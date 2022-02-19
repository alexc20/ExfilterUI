from django.urls import include, path
from rest_framework import routers
from . import views

app_name = "eventapi"

router = routers.DefaultRouter()
router.register(r'egressevents', views.EgressEventViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]