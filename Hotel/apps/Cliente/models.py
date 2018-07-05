from django.db import models

# Create your models here.
class Nacionalidad (models.Model):
    idNacionalidad=models.CharField(primary_key=True,max_length=100)
    pais=models.CharField(max_length=200)
    nacionalidad=models.CharField(max_length=200)

class Cliente (models.Model):
    idCLiente=models.CharField(primary_key=True,max_length=100)
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)#no creo que deba ir
    documento=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    fkNacionalidad=models.ForeignKey(Nacionalidad,on_delete=None)
