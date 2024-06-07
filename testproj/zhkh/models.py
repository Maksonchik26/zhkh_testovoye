from django.db import models


class House(models.Model):
    address = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f"ID: {self.id}. Addr: {self.address}"


class Flat(models.Model):
    house = models.ForeignKey(House, related_name="flats", on_delete=models.CASCADE)
    number = models.IntegerField()
    area = models.FloatField()

    class Meta:
        unique_together = ('house', 'number')

    def __str__(self):
        return f"ID: {self.id}. Number: {self.number}"


class WaterMeter(models.Model):
    flat = models.ForeignKey(Flat, related_name="water_meters", on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    class Meta:
        unique_together = ('flat', 'name')
    def __str__(self):
        return f"ID: {self.id}. Flat ID: {self.flat_id}. Name: {self.name}"


class WaterMeterReading(models.Model):
    water_meter = models.ForeignKey(WaterMeter, related_name="water_meter_readings", on_delete=models.CASCADE)
    date = models.DateField()
    reading = models.FloatField()

    def __str__(self):
        return f"ID: {self.id}. Water Meter ID: {self.water_meter_id}. Date: {self.date}"


class Tariff(models.Model):
    NAMES = (
        ('WATER', 'Water'),
        ('MAINTENANCE', 'Maintenance'),
    )
    name = models.CharField(max_length=128, choices=NAMES)
    unit_price = models.FloatField()

    def __str__(self):
        return f"ID: {self.id}. Name: {self.name}. Unit Price: {self.unit_price}"


class CalculationProgress(models.Model):
    STATUSES = (
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
    )
    task_id = models.CharField(max_length=256, unique=True)
    progress = models.IntegerField(default=0)
    status = models.CharField(max_length=256, choices=STATUSES, default="Pending")

    def __str__(self):
        return f"ID: {self.id}. Task ID: {self.task_id}. Status: {self.status}"


class FlatRentCalculation(models.Model):
    flat = models.ForeignKey(Flat, related_name='flat_rent_calculations', on_delete=models.CASCADE)
    water_rent = models.FloatField()
    maintenance_rent = models.FloatField()
    total_rent = models.FloatField()
    month = models.CharField(max_length=7)

    def __str__(self):
        return f"ID: {self.id}. Flat ID: {self.flat_id}. Month: {self.month}, Total rent: {self.total_rent}"
