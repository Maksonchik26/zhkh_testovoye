from django.db import models


#TODO подумать над возможностью добавить частные и многоквартирные дома (чек про валидацию)
class House(models.Model):
    address = models.CharField(max_length=256)

    def __str__(self):
        return f"ID: {self.id}. Addr: {self.address}"


class Flat(models.Model):
    house = models.ForeignKey(House, related_name="flats", on_delete=models.CASCADE)
    number = models.IntegerField()
    area = models.FloatField()

    def __str__(self):
        return f"ID: {self.id}. Number: {self.number}"


class WaterMeter(models.Model):
    flat = models.ForeignKey(Flat, related_name="water_meters", on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"ID: {self.id}. Flat ID: {self.flat_id}. Name: {self.name}"


# TODO мб переименовать модель
class WaterMeterReading(models.Model):
    water_meter = models.ForeignKey(WaterMeter, related_name="water_meter_readings", on_delete=models.CASCADE)
    date = models.DateTimeField()
    reading = models.FloatField()

    def __str__(self):
        return f"ID: {self.id}. Water Meter ID: {self.water_meter_id}. Date: {self.date}"


# TODO сделать чойсес: water, maintenance
class Tariff(models.Model):
    name = models.CharField(max_length=128)
    unit_price = models.FloatField()

    def __str__(self):
        return f"ID: {self.id}. Name: {self.name}. Unit Price: {self.unit_price}"
