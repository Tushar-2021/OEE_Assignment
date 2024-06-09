from django.db import models

class Machine(models.Model):
    machine_name = models.CharField(max_length=100)
    machine_serial_no = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)

    def calculate_oee(self):
        logs = ProductionLog.objects.filter(machine=self)
        if not logs.exists():
            return None

        available_time = 3 * 8  # 3 shifts, 8 hours each
        ideal_cycle_time = 5 / 60  # 5 minutes converted to hours
        actual_output = logs.count()
        available_operating_time = actual_output * ideal_cycle_time
        unplanned_downtime = available_time - available_operating_time

        if available_time == 0:
            availability = 0
        else:
            availability = ((available_time - unplanned_downtime) / available_time) * 100

        if available_operating_time == 0:
            performance = 0
        else:
            performance = (ideal_cycle_time * actual_output / available_operating_time) * 100

        good_product_count = sum(1 for log in logs if log.actual_duration == ideal_cycle_time)
        total_product_count = logs.count()

        if total_product_count == 0:
            quality = 0
        else:
            quality = (good_product_count / total_product_count) * 100

        return {
            'availability': availability,
            'performance': performance,
            'quality': quality,
            'oee': (availability * performance * quality) / 10000
        }

class ProductionLog(models.Model):
    cycle_no = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=100)
    material_name = models.CharField(max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.FloatField()

    @property
    def actual_duration(self):
        return (self.end_time - self.start_time).total_seconds() / 3600
