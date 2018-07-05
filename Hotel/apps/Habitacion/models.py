from django.db import models

# Create your models here.
class Tipo_habitacion (models.Model):
    idTipo=models.CharField(max_length=100,primary_key=True)
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField()

class Habitacion (models.Model):
    idHabitacion=models.IntegerField(primary_key=True)
    numero=models.IntegerField(default=0)
    estado=models.BooleanField(default=False)
    costo=models.IntegerField(default=0)
    descripcion=models.TextField()
    fkTipo=models.ForeignKey(Tipo_habitacion,on_delete=None)
