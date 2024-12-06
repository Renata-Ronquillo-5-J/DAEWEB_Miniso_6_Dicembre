from django.db import models

# Create your models here.
class Productos (models.Model):
    Id_Producto=models.IntegerField(primary_key=True)
    Nombre_Producto=models.CharField(max_length=100)
    Stock=models.IntegerField()
    Id_Proveedor=models.CharField(max_length=100)
    Precio_Venta=models.IntegerField()
    Precio_Mayoreo=models.IntegerField()
    Descripcion=models.CharField(max_length=300)

    def __str__(self):
        return self.Nombre_Producto
    

    
    