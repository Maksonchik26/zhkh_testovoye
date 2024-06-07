from datetime import datetime
from celery import shared_task
import calendar

from .models import Tariff, WaterMeterReading, House, CalculationProgress, FlatRentCalculation


@shared_task(bind=True)
def calculate_rent(self, house_id, month):
    house = House.objects.get(id=house_id)
    flats = house.flats.all()
    water_tariff = Tariff.objects.get(name="WATER")
    maintenance_tariff = Tariff.objects.get(name="MAINTENANCE")

    progress, created = CalculationProgress.objects.get_or_create(task_id=self.request.id)
    month_start = datetime.strptime(month, "%Y-%m").date()

    # Get last day of month
    last_day = calendar.monthrange(month_start.year, month_start.month)[1]
    month_end = month_start.replace(day=last_day)
    processed_flats = 0

    for flat in flats:
        flat_water_rent = 0
        for water_meter in flat.water_meters.all():
            previous_reading = WaterMeterReading.objects.filter(water_meter=water_meter, date=month_start).first()
            current_reading = WaterMeterReading.objects.filter(water_meter=water_meter, date=month_end).first()
            usage = current_reading.reading - previous_reading.reading
            flat_water_rent += usage * water_tariff.unit_price

        flat_maintenance_rent = flat.area * maintenance_tariff.unit_price
        total_flat_rent = flat_water_rent + flat_maintenance_rent

        FlatRentCalculation.objects.create(
            flat=flat,
            water_rent=flat_water_rent,
            maintenance_rent=flat_maintenance_rent,
            total_rent=total_flat_rent,
            month=month
        )

        processed_flats += 1
        progress.progress = processed_flats / len(flats)
        progress.save(update_fields=['progress'])

    progress.status = 'completed'
    progress.save(update_fields=['status'])
    return house.id
