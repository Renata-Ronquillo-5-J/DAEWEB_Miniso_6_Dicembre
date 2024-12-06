
from django.db import models

# Create your models here.
class Empleados(models.Model):
    Id_Empleados=models.IntegerField(primary_key=True)
    Nombre=models.CharField(max_length=100)
    No_Telefono=models.IntegerField()
    Correo=models.CharField(max_length=100)
    Fecha_Nacimiento=models.DateField()
    Salario=models.IntegerField()
    Direccion=models.CharField(max_length=300)

    def __str__(self):
        return str(self.Id_Empleados)