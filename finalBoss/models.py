from django.db import models

# Create your models here.


class RawData(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.DateField()


class TransformedData(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=255)
    edad_nominal = models.IntegerField()
