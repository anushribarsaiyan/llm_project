from rest_framework import serializers
from .models import ProcessedResult

class ProcessedResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessedResult
        fields = ['id', 'input_text', 'result', 'task', 'created_at']
