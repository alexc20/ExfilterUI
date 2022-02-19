# serializers.py

from rest_framework import serializers

from .models import EgressEvent

class EgressEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EgressEvent
        fields = ('Pid','Saddr', 'Daddr', 'Data', 'Msg', 'Timestamp_ns')