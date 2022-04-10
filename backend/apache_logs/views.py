from django.shortcuts import render
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from .models import ApacheLog
from . serializers import ApacheLogsSerializer


class ApacheLogViewSet(GenericViewSet, ListModelMixin):
    permission_classes = [AllowAny]
    queryset = ApacheLog.objects
    serializer_class = ApacheLogsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {
        'ip': ['exact', 'contains'],
        'date': ['exact', 'lte', 'gte', 'lt', 'gt'],
    }
