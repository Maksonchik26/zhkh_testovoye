from django.http import HttpResponse
from rest_framework import generics, viewsets

from .models import House, Flat, Tariff, WaterMeter, WaterMeterReading
from .serializers import HouseAddrSerializer, FlatSerializer, WaterMeterSerializer, WaterMeterReadingSerializer, \
    TariffSerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseAddrSerializer


class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class WaterMeterViewSet(viewsets.ModelViewSet):
    queryset = WaterMeter.objects.all()
    serializer_class = WaterMeterSerializer


class WaterMeterReadingViewSet(viewsets.ModelViewSet):
    queryset = WaterMeterReading.objects.all()
    serializer_class = WaterMeterReadingSerializer


class TariffViewSet(viewsets.ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
