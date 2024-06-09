from rest_framework import serializers
from .models import Machine, ProductionLog

class MachineSerializer(serializers.ModelSerializer):
    oee = serializers.SerializerMethodField()

    class Meta:
        model = Machine
        fields = ['machine_name', 'machine_serial_no', 'time', 'oee']

    def get_oee(self, obj):
        return obj.calculate_oee()

class ProductionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionLog
        fields = '__all__'
