from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import RawDataSerializer, TransformedDataSerializer
from .models import RawData, TransformedData

import datetime


# Create your views here.


class RawDataViewSet(viewsets.ModelViewSet):
    queryset = RawData.objects.all()
    serializer_class = RawDataSerializer


class TransformedDataViewSet(viewsets.ModelViewSet):
    queryset = TransformedData.objects.all()
    serializer_class = TransformedDataSerializer

    def create(self, request):
        # Obtener datos del request
        nombre = request.data['nombre']
        apellido = request.data['apellido']
        fecha_nacimiento = request.data['fecha_nacimiento']

        # Calcular edad nominal
        fecha_nacimiento = datetime.datetime.strptime(
            fecha_nacimiento, '%Y-%m')
        edad_actual = datetime.datetime.now()
        edad_nominal = edad_actual.year - fecha_nacimiento.year

        # Crear nombre completo
        nombre_completo = f'{nombre} {apellido}'

        # Crear y guardar la instancia del modelo
        transformed_data = TransformedData.objects.create(
            nombre_completo=nombre_completo,
            edad_nominal=edad_nominal
        )

        # Serializar y retornar la instancia
        serializer = TransformedDataSerializer(transformed_data)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # Obtener instancia del modelo por ID
        transformed_data = TransformedData.objects.get(pk=pk)

        # Serializar y retornar la instancia
        serializer = TransformedDataSerializer(transformed_data)
        return Response(serializer.data)
