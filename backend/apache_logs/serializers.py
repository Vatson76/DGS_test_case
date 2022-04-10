from rest_framework import serializers
from .models import ApacheLog


class ApacheLogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApacheLog
        fields = '__all__'
