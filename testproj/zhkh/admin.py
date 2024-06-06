from django.contrib import admin

from .models import House, Flat, Tariff, WaterMeter, WaterMeterReading

admin.site.register(House)
admin.site.register(Flat)
admin.site.register(WaterMeter)
admin.site.register(WaterMeterReading)
admin.site.register(Tariff)
