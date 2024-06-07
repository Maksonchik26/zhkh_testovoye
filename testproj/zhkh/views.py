from rest_framework import viewsets

from .models import Flat, Tariff, WaterMeter, WaterMeterReading, FlatRentCalculation
from .serializers import HouseAddrSerializer, FlatSerializer, WaterMeterSerializer, WaterMeterReadingSerializer, \
    TariffSerializer, FlatRentCalculationSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import calculate_rent
from .models import CalculationProgress, House


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseAddrSerializer


class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

    def get_queryset(self):
        house_id = self.kwargs.get('house_pk')
        return self.queryset.filter(house_id=house_id)


class WaterMeterViewSet(viewsets.ModelViewSet):
    queryset = WaterMeter.objects.all()
    serializer_class = WaterMeterSerializer

    def get_queryset(self):
        flat_id = self.kwargs.get('flat_pk')
        return self.queryset.filter(flat_id=flat_id)


class WaterMeterReadingViewSet(viewsets.ModelViewSet):
    queryset = WaterMeterReading.objects.all()
    serializer_class = WaterMeterReadingSerializer

    def get_queryset(self):
        water_meter_id = self.kwargs.get('water_meter_pk')
        return self.queryset.filter(water_meter_id=water_meter_id)


class TariffViewSet(viewsets.ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


class FlatRentCalculationViewSet(viewsets.ModelViewSet):
    queryset = FlatRentCalculation.objects.all()
    serializer_class = FlatRentCalculationSerializer


@api_view(['POST'])
def start_rent_calculation(request, house_id):
    house = House.objects.get(id=house_id)
    month = request.query_params.get('month')
    if not month:
        return Response({'error': 'Month parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
    task = calculate_rent.delay(house.id, month)
    return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def get_task_progress(request, task_id):
    progress = CalculationProgress.objects.get(task_id=task_id)
    data = {
        'total_flats': progress.total_flats,
        'processed_flats': progress.processed_flats,
        'status': progress.status
    }
    return Response(data, status=status.HTTP_200_OK)
