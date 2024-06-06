from testproj.zhkh.models import Tariff, WaterMeter, WaterMeterReading


def сalculate_water_bill(unit_price: float, readings: list[WaterMeterReading]) -> float:
    if len(readings) >= 2:
        latest_reading = readings[-1]
        previous_reading = readings[-2]
        bill = (latest_reading - previous_reading) * unit_price
        return bill


def calculate_maintenance_fee(area: float, unit_price: float) -> float:
    return area * unit_price

