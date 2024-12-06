
from django.shortcuts import render,redirect
from .models import Ventas

# Create your views here.
def inicio_vista(request):
    LasVentas=Ventas.objects.all()
    return render (request,"GestionarVentas.html", {"MisVentas":LasVentas})

def RegistrarVentas(request):
    Id_Venta=request.POST["numVenta"]
    Id_Empleado=request.POST["numEmpleado"]
    Id_Producto=request.POST["numProducto"]
    NombreProducto=request.POST["txtNombreProducto"]
    Cantidad=request.POST["numCantidad"]
    Total=request.POST["numTotal"]
    FechaVenta=request.POST["txtFechaVenta"]



    GuardarVenta=Ventas.objects.create(
        Id_Venta=Id_Venta, Id_Empleado=Id_Empleado, Id_Producto=Id_Producto, NombreProducto=NombreProducto,Cantidad=Cantidad,Total=Total,FechaVenta=FechaVenta
    ) # GUARDA EL REGISTRO

    return redirect("Ventas")

def SeleccionarVentas(request,Id_Venta):
    Venta=Ventas.objects.get(Id_Venta=Id_Venta)
    return render(request,"EditarVentas.html",{"MisVentas":Venta})

def EditarVentas(request):

    Id_Venta=request.POST["numVenta"]
    Id_Empleado=request.POST["numEmpleado"]
    Id_Producto=request.POST["numProducto"]
    NombreProducto=request.POST["txtNombreProducto"]
    Cantidad=request.POST["numCantidad"]
    Total=request.POST["numTotal"]
    FechaVenta=request.POST["txtFechaVenta"]

    Venta=Ventas.objects.get(Id_Venta=Id_Venta)
    Venta.Id_Venta=Id_Venta
    Venta.Id_Empleado=Id_Empleado
    Venta.Id_Producto=Id_Producto
    Venta.NombreProducto=NombreProducto
    Venta.Cantidad=Cantidad
    Venta.Total=Total
    Venta.FechaVenta=FechaVenta
    Venta.save() #guardar registro actualizado
    return redirect("Ventas")

def BorrarVentas(request,Id_Venta):
    Venta=Ventas.objects.get(Id_Venta=Id_Venta)
    Venta.delete()
    return redirect("Ventas")


