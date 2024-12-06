
from django.shortcuts import render,redirect
from .models import Sucursales

# Create your views here.
def inicio_vista(request):
    LasSucursales=Sucursales.objects.all()
    return render (request,"GestionarSucursales.html", {"MisSucursales":LasSucursales})

def RegistrarSucursales(request):
    Id_Sucursal=request.POST["numSucursal"]
    Ubicacion=request.POST["txtDireccion"]
    Correo=request.POST["txtCorreo"]
    Telefono=request.POST["numTelefono"]
    Ciudad=request.POST["txtCiudad"]
    Estado=request.POST["txtEstado"]
    Horario=request.POST["txtHorario"]



    GuardarSucursales=Sucursales.objects.create(
        Id_Sucursal=Id_Sucursal,Ubicacion=Ubicacion,Correo=Correo, Telefono=Telefono, Ciudad=Ciudad, Estado=Estado,Horario=Horario
    ) # GUARDA EL REGISTRO

    return redirect("Sucursales")

def SeleccionarSucursales(request,Id_Sucursal):
    Sucursal=Sucursales.objects.get(Id_Sucursal=Id_Sucursal)
    return render(request,"EditarSucursales.html",{"MisSucursales":Sucursal})

def EditarSucursales(request):

    Id_Sucursal=request.POST["numSucursal"]
    Ubicacion=request.POST["txtDireccion"]
    Correo=request.POST["txtCorreo"]
    Telefono=request.POST["numTelefono"]
    Ciudad=request.POST["txtCiudad"]
    Estado=request.POST["txtEstado"]
    Horario=request.POST["txtHorario"]

    Sucursal=Sucursales.objects.get(Id_Sucursal=Id_Sucursal)
    Sucursal.Id_Sucursal=Id_Sucursal
    Sucursal.Ubicacion=Ubicacion
    Sucursal.Correo=Correo
    Sucursal.Telefono=Telefono
    Sucursal.Ciudad=Ciudad
    Sucursal.Estado=Estado
    Sucursal.Horario=Horario
    Sucursal.save() #guardar registro actualizado
    return redirect("Sucursales")

def BorrarSucursales(request,Id_Sucursal):
    Sucursal=Sucursales.objects.get(Id_Sucursal=Id_Sucursal)
    Sucursal.delete()
    return redirect("Sucursales")

