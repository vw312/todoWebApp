from rest_framework import serializers
from .models import Schedules

class scheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = '__all__'
