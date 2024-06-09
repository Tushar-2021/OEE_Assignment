from django.test import TestCase
from rest_framework.test import APIClient
from .models import Machine, ProductionLog
from django.utils import timezone
from datetime import timedelta

class MachineTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.machine = Machine.objects.create(machine_name="Test Machine", machine_serial_no="12345")

    def test_create_machine(self):
        response = self.client.post('/api/machines/', {'machine_name': 'New Machine', 'machine_serial_no': '67890'})
        self.assertEqual(response.status_code, 201)

    def test_calculate_oee(self):
        start_time = timezone.now()
        end_time = start_time + timedelta(minutes=5)
        ProductionLog.objects.create(cycle_no="CN001", unique_id="UID001", material_name="Material A", machine=self.machine, start_time=start_time, end_time=end_time, duration=5/60)

        response = self.client.get(f'/api/machines/{self.machine.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('oee', response.data)

class ProductionLogTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.machine = Machine.objects.create(machine_name="Test Machine", machine_serial_no="12345")

    def test_create_production_log(self):
        start_time = timezone.now()
        end_time = start_time + timedelta(minutes=5)
        response = self.client.post('/api/production_logs/', {
            'cycle_no': 'CN001',
            'unique_id': 'UID001',
            'material_name': 'Material A',
            'machine': self.machine.id,
            'start_time': start_time,
            'end_time': end_time,
            'duration': 5/60
        })
        self.assertEqual(response.status_code, 201)
