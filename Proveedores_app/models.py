from django.db import models

# Create your models here.
class Proveedores(models.Model):
    Id_Proveedor=models.IntegerField(primary_key=True)
    Telefono=models.IntegerField()
    Correo=models.CharField(max_length=100)
    Ciudad=models.CharField(max_length=100)
    Id_ProductoV=models.IntegerField()
    PrecioProducto=models.IntegerField()
    NombreProducto=models.CharField(max_length=300)

    def __str__(self):
        return self.Id_Proveedor