from django.shortcuts import render,redirect
from .models import Clientes

# Create your views here.
def inicio_vista(request):
    LosClientes=Clientes.objects.all()
    return render (request,"GestionarClientes.html", {"MisClientes":LosClientes})

def RegistrarClientes(request):
    Id_Cliente=request.POST["numCliente"]
    No_Telefono=request.POST["numTelefono"]
    Fecha_Nacimiento=request.POST["DateFecha"]
    Correo=request.POST["txtCorreo"]
    Nombre=request.POST["txtNombre"]
    Direccion=request.POST["txtDireccion"]
    Sexo=request.POST["txtSexo"]



    GuardarClientes=Clientes.objects.create(
        Id_Cliente=Id_Cliente, No_Telefono=No_Telefono, Fecha_Nacimiento=Fecha_Nacimiento, Correo=Correo, Nombre=Nombre, Direccion=Direccion, Sexo=Sexo
    ) # GUARDA EL REGISTRO

    return redirect("Clientes")

def SeleccionarClientes(request,Id_Cliente):
    Cliente=Clientes.objects.get(Id_Cliente=Id_Cliente)
    return render(request,"EditarClientes.html",{"MisClientes":Cliente})

def EditarClientes(request):

    Id_Cliente=request.POST["numCliente"]
    No_Telefono=request.POST["numTelefono"]
    Fecha_Nacimiento=request.POST["DateFecha"]
    Correo=request.POST["txtCorreo"]
    Nombre=request.POST["txtNombre"]
    Direccion=request.POST["txtDireccion"]
    Sexo=request.POST["txtSexo"]


    Cliente=Clientes.objects.get(Id_Cliente=Id_Cliente)
    Cliente.Id_Cliente=Id_Cliente
    Cliente.No_Telefono=No_Telefono
    Cliente.Fecha_Nacimiento=Fecha_Nacimiento
    Cliente.Correo=Correo
    Cliente.Nombre=Nombre
    Cliente.Direccion=Direccion
    Cliente.Sexo=Sexo
    Cliente.save() #guardar registro actualizado
    return redirect("Clientes")

def BorrarClientes(request,Id_Cliente):
    Cliente=Clientes.objects.get(Id_Cliente=Id_Cliente)
    Cliente.delete()
    return redirect("Clientes")

