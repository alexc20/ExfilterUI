from django.db import models

# Create your models here.
class EgressEvent(models.Model):
    Pid = models.IntegerField()
    Saddr = models.CharField(max_length=255)
    Daddr = models.CharField(max_length=255)
    Data = models.TextField()
    Msg = models.CharField(max_length=255)
    Timestamp_ns = models.DateTimeField()