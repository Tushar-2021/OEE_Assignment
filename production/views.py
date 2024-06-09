from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Machine, ProductionLog
from .serializers import MachineSerializer, ProductionLogSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import filters

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['machine_name', 'time']
    ordering_fields = ['time']

class ProductionLogViewSet(viewsets.ModelViewSet):
    queryset = ProductionLog.objects.all()
    serializer_class = ProductionLogSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['cycle_no', 'material_name', 'machine__machine_name']
    ordering_fields = ['start_time']
