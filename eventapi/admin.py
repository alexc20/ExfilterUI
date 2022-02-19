from django.contrib import admin

# Register your models here.
from .models import EgressEvent

admin.site.register(EgressEvent)
