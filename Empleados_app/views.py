from django.shortcuts import render,redirect
from .models import Empleados

# Create your views here.
def inicio_vista(request):
    LosEmpleados=Empleados.objects.all()
    return render (request,"GestionarEmpleados.html", {"MisEmpleados":LosEmpleados})

def RegistrarEmpleados(request):
    Id_Empleados=request.POST["numEmpleados"]
    Nombre=request.POST["txtNombre"]
    No_Telefono=request.POST["numTelefono"]
    Correo=request.POST["txtCorreo"]
    Fecha_Nacimiento=request.POST["DateFecha"]
    Salario=request.POST["numSalario"]
    Direccion=request.POST["txtDireccion"]



    GuardarEmpleados=Empleados.objects.create(
        Id_Empleados=Id_Empleados, Nombre=Nombre, No_Telefono=No_Telefono, Correo=Correo, Fecha_Nacimiento=Fecha_Nacimiento, Salario=Salario, Direccion=Direccion
    ) # GUARDA EL REGISTRO

    return redirect("Empleados")

def SeleccionarEmpleados(request,Id_Empleados):
    Empleado=Empleados.objects.get(Id_Empleados=Id_Empleados)
    return render(request,"EditarEmpleados.html",{"MisEmpleados":Empleado})

def EditarEmpleados(request):

    Id_Empleados=request.POST["numEmpleados"]
    Nombre=request.POST["txtNombre"]
    No_Telefono=request.POST["numTelefono"]
    Correo=request.POST["txtCorreo"]
    Fecha_Nacimiento=request.POST["DateFecha"]
    Salario=request.POST["numSalario"]
    Direccion=request.POST["txtDireccion"]


    Empleado=Empleados.objects.get(Id_Empleados=Id_Empleados)
    Empleado.Id_Empleados=Id_Empleados
    Empleado.Nombre=Nombre
    Empleado.No_Telefono=No_Telefono
    Empleado.Correo=Correo
    Empleado.Fecha_Nacimiento=Fecha_Nacimiento
    Empleado.Salario=Salario
    Empleado.Direccion= Direccion
    Empleado.save() #guardar registro actualizado
    return redirect("Empleados")

def BorrarEmpleados(request,Id_Empleados):
    Empleado=Empleados.objects.get(Id_Empleados=Id_Empleados)
    Empleado.delete()
    return redirect("Empleados")
