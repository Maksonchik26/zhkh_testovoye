from rest_framework import serializers

from .models import House, Flat, Tariff, WaterMeter, WaterMeterReading


class WaterMeterReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterMeterReading
        fields = "__all__"


class WaterMeterSerializer(serializers.ModelSerializer):
    readings = WaterMeterReadingSerializer(many=True, read_only=True)

    class Meta:
        model = WaterMeter
        fields = "__all__"


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = "__all__"


class FlatSerializer(serializers.ModelSerializer):
    water_meters = WaterMeterReadingSerializer(many=True, read_only=True)

    class Meta:
        model = Flat
        fields = "__all__"


class HouseAddrSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = ["id", "address"]
