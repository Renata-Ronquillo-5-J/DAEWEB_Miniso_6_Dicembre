from django.shortcuts import render,redirect
from .models import Productos

# Create your views here.
def inicio_vista(request):
    LosProductos=Productos.objects.all()
    return render (request,"GestionarProducto.html", {"MisProductos":LosProductos})

def RegistrarProductos(request):
    Id_Producto=request.POST["numProducto"]
    Nombre_Producto=request.POST["txtNombre"]
    Stock=request.POST["numStock"]
    Id_Proveedor=request.POST["txtProveedor"]
    Precio_Venta=request.POST["numPrecioVenta"]
    Precio_Mayoreo=request.POST["numPrecioMayoreo"]
    Descripcion=request.POST["txtDescripcion"]



    GuiardarProductos=Productos.objects.create(
        Id_Producto=Id_Producto,Nombre_Producto=Nombre_Producto, Stock=Stock, Id_Proveedor=Id_Proveedor,Precio_Venta=Precio_Venta, Precio_Mayoreo=Precio_Mayoreo, Descripcion=Descripcion
    ) # GUARDA EL REGISTRO

    return redirect("Productos")

def SeleccionarProductos(request,Id_Producto):
    Producto=Productos.objects.get(Id_Producto=Id_Producto)
    return render(request,"EditarProducto.html",{"MisProductos":Producto})

def EditarProducto(request):
    Id_Producto=request.POST["numProducto"]
    Nombre_Producto=request.POST["txtNombre"]
    Stock=request.POST["numStock"]
    Id_Proveedor=request.POST["txtProveedor"]
    Precio_Venta=request.POST["numPrecioVenta"]
    Precio_Mayoreo=request.POST["numPrecioMayoreo"]
    Descripcion=request.POST["txtDescripcion"]

    Producto=Productos.objects.get(Id_Producto=Id_Producto)
    Producto.Nombre_Producto=Nombre_Producto
    Producto.Stock=Stock
    Producto.Id_Proveedor=Id_Proveedor
    Producto.Precio_Venta=Precio_Venta
    Producto.Precio_Mayoreo=Precio_Mayoreo
    Producto.Descripcion=Descripcion
    Producto.save() #guardar registro actualizado
    return redirect("Productos")

def BorrarProductos(request,Id_Producto):
    Producto=Productos.objects.get(Id_Producto=Id_Producto)
    Producto.delete()
    return redirect("Productos")
