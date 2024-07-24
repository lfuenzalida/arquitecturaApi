from rest_framework import serializers
from .models import RawData, TransformedData


class RawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawData
        fields = '__all__'
        many = True


class TransformedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransformedData
        fields = '__all__'
        many = True
