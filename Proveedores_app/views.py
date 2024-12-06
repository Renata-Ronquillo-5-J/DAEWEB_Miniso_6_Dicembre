
from django.shortcuts import render,redirect
from .models import Proveedores

# Create your views here.
def inicio_vista(request):
    LosProveedores=Proveedores.objects.all()
    return render (request,"GestionarProveedores.html", {"MisProveedores":LosProveedores})

def RegistrarProveedores(request):
    Id_Proveedor=request.POST["numProveedor"]
    Telefono=request.POST["numTelefono"]
    Correo=request.POST["txtCorreo"]
    Ciudad=request.POST["txtCiudad"]
    Id_ProductoV=request.POST["numIdPro"]
    PrecioProducto=request.POST["numPrecioPro"]
    NombreProducto=request.POST["txtNombrePro"]



    GuardarProveedores=Proveedores.objects.create(
        Id_Proveedor=Id_Proveedor,Telefono=Telefono, Correo=Correo, Ciudad=Ciudad, Id_ProductoV=Id_ProductoV, PrecioProducto=PrecioProducto, NombreProducto=NombreProducto
    ) # GUARDA EL REGISTRO

    return redirect("Proveedores")

def SeleccionarProveedores(request,Id_Proveedor):
    Proveedor=Proveedores.objects.get(Id_Proveedor=Id_Proveedor)
    return render(request,"EditarProveedores.html",{"MisProveedores":Proveedor})

def EditarProveedores(request):

    Id_Proveedor=request.POST["numProveedor"]
    Telefono=request.POST["numTelefono"]
    Correo=request.POST["txtCorreo"]
    Ciudad=request.POST["txtCiudad"]
    Id_ProductoV=request.POST["numIdPro"]
    PrecioProducto=request.POST["numPrecioPro"]
    NombreProducto=request.POST["txtNombrePro"]




    Proveedor=Proveedores.objects.get(Id_Proveedor=Id_Proveedor)
    Proveedor.Id_Proveedor=Id_Proveedor
    Proveedor.Telefono=Telefono
    Proveedor.Correo=Correo
    Proveedor.Ciudad=Ciudad
    Proveedor.Id_ProductoV=Id_ProductoV
    Proveedor.PrecioProducto=PrecioProducto
    Proveedor.NombreProducto=NombreProducto
    Proveedor.save() #guardar registro actualizado
    return redirect("Proveedores")

def BorrarProveedores(request,Id_Proveedor):
    Proveedor=Proveedores.objects.get(Id_Proveedor=Id_Proveedor)
    Proveedor.delete()
    return redirect("Proveedores")
