from django.urls import path, include
from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter
from .views import *

# LVL 1
# House routers
house_router = routers.SimpleRouter()
house_router.register(r'houses', HouseViewSet)

# Tariff routers
tariff_routers = routers.SimpleRouter()
tariff_routers.register(r'tariffs', TariffViewSet)


## LVL 2
# Flat routers
flat_router = NestedSimpleRouter(house_router, r'houses', lookup='house')
flat_router.register(r'flats', FlatViewSet, basename='house-flats')


### LVL 3
# Water Meter routers
water_meter_router = NestedSimpleRouter(flat_router, r'flats', lookup='flat')
water_meter_router.register(r'water-meters', WaterMeterViewSet, basename='water-meters')


#### LVL 4
water_meter_readings_router = NestedSimpleRouter(water_meter_router, r'water-meters', lookup='water_meter')
water_meter_readings_router.register(r'water-meter-readings', WaterMeterReadingViewSet, basename='water-meter-readings')

urlpatterns = [
    path('start-rent-calculation/<int:house_id>', start_rent_calculation),
    path('', include(house_router.urls)),
    path('', include(tariff_routers.urls)),
    path('', include(flat_router.urls)),
    path('', include(water_meter_router.urls)),
    path('', include(water_meter_readings_router.urls)),
    path('calculate-progress/<str:task_id>/', get_task_progress),
]
