from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EgressEventSerializer
from .models import EgressEvent

# Create your views here.
class EgressEventViewSet(viewsets.ModelViewSet):
    queryset = EgressEvent.objects.all().order_by('Timestamp_ns')
    serializer_class = EgressEventSerializer

