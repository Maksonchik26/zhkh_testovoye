from django.contrib import admin

from .models import House, Flat, Tariff, WaterMeter, WaterMeterReading, CalculationProgress, FlatRentCalculation

admin.site.register(House)
admin.site.register(Flat)
admin.site.register(WaterMeter)
admin.site.register(WaterMeterReading)
admin.site.register(Tariff)
admin.site.register(CalculationProgress)
admin.site.register(FlatRentCalculation)
