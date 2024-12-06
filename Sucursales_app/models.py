from django.db import models

# Create your models here.
class Sucursales(models.Model):
    Id_Sucursal=models.IntegerField(primary_key=True)
    Ubicacion=models.CharField(max_length=300)
    Correo=models.CharField(max_length=100)
    Telefono=models.IntegerField()
    Ciudad=models.CharField(max_length=300)
    Estado=models.CharField(max_length=300)
    Horario=models.CharField(max_length=300)

    def __str__(self):
        return self.Id_Sucursal