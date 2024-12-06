from django.db import models

# Create your models here.
class Ventas(models.Model):
    Id_Venta=models.IntegerField(primary_key=True)
    Id_Empleado=models.IntegerField()
    Id_Producto=models.IntegerField()
    NombreProducto=models.CharField(max_length=300)
    Cantidad=models.IntegerField()
    Total=models.IntegerField()
    FechaVenta=models.DateField()

    def __str__(self):
        return self.Id_Venta