from django.db import models

class Registrador (models.Model):
        idRegistrador=models.CharField(primary_key=True,max_length=100)
        nombre=models.CharField(max_length=100)
        direccion=models.CharField(max_length=100)#no creo que deba ir
        documento=models.CharField(max_length=100)
        telefono=models.CharField(max_length=100)
        estado=models.BooleanField(default=False)
        observacion=models.TextField()
