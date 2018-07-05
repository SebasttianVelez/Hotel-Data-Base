from django.db import models
from apps.Habitacion.models import Habitacion
from apps.Cliente.models import Cliente
from apps.Registrador.models import Registrador
class Estado (models.Model):
    idEstado=models.CharField(primary_key=True,max_length=100)
    nombre=models.CharField(max_length=100)
class Alquiler (models.Model):
    idAlquiler=models.CharField(max_length=200,primary_key=True)
    fechaHoraEntrada=models.DateTimeField(auto_now_add=True)
    fechaHoraSalida=models.DateTimeField()
    costoTotal=models.IntegerField(default=0)#change for real cost
    observacion=models.TextField()
    fkHabitacion=models.ForeignKey(Habitacion,on_delete=None,null=False)
    fkCliente=models.ForeignKey(Cliente,on_delete=None,null=False)
    fkRegistrador=models.ForeignKey(Registrador,on_delete=None,null=False)
    fkEstado=models.ForeignKey(Estado,on_delete=None,null=True)
