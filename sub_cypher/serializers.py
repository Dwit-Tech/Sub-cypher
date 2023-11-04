from rest_framework import serializers
from sub_cypher.models import LogEntry

class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = '__all__'
