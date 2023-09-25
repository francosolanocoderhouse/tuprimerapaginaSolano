from django.db import models

# Create your models here.
class vendedor(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    numero_empleado= models.IntegerField()
    
class venta(models.Model):
    fecha= models.DateField() 
    monto= models.FloatField()
    numero_vendedor= models.IntegerField()

class cliente(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    numero_cliente= models.IntegerField()

