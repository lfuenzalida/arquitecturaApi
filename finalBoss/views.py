from django.forms import ValidationError
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import RawDataSerializer, TransformedDataSerializer
from .models import RawData, TransformedData
import datetime


def transform_raw_data(raw_data):
    transformed_data = {}
    transformed_data['full_name'] = f"{raw_data['nombre']} {raw_data['apellido']}"

    try:
        birth_date = datetime.datetime.strptime(
            raw_data['fecha_nacimiento'], '%Y-%m-%d')
    except ValueError:
        raise ValidationError("Invalid date format. Please use YYYY-MM-DD.")

    transformed_data['edad'] = calculate_age(
        birth_date)  # Implement calculate_age function

    return transformed_data


class RawDataViewSet(viewsets.ModelViewSet):
    queryset = RawData.objects.all()
    serializer_class = RawDataSerializer


class TransformedDataViewSet(viewsets.ModelViewSet):
    queryset = TransformedData.objects.all()
    serializer_class = TransformedDataSerializer

    def create(self, request):
        serializer = TransformedDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            transformed_data = transform_raw_data(serializer.validated_data)
        except ValidationError as e:
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)

        transformed_data_instance = TransformedData.objects.create(
            **transformed_data)
        serializer = TransformedDataSerializer(transformed_data_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        transformed_data = TransformedData.objects.get(pk=pk)
        serializer = TransformedDataSerializer(transformed_data)
        return Response(serializer.data)
