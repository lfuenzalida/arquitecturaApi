from rest_framework import serializers
from .models import RawData, TransformedData


class RawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawData
        fields = '__all__'


class TransformedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransformedData
        fields = '__all__'
