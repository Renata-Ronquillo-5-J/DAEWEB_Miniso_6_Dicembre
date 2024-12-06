
from django.db import models

# Create your models here.
class Clientes(models.Model):
    Id_Cliente=models.IntegerField(primary_key=True)
    No_Telefono=models.IntegerField()
    Fecha_Nacimiento=models.DateField()
    Correo=models.CharField(max_length=100)
    Nombre=models.CharField(max_length=100)
    Direccion=models.CharField(max_length=100)
    Sexo=models.CharField(max_length=300)

    def __str__(self):
        return self.Id_Cliente