from django.urls import path 
from Empleados_app import views

urlpatterns = [
    path("Empleados",views.inicio_vista,name="Empleados"),
    path("RegistrarEmpleados/",views.RegistrarEmpleados,name="RegistrarEmpleados"),
    path("SeleccionarEmpleados/<Id_Empleados>",views.SeleccionarEmpleados,name="SeleccionarEmpleados"),
    path("EditarEmpleados/",views.EditarEmpleados,name="EditarEmpleados"),
    path("BorrarEmpleados/<Id_Empleados>",views.BorrarEmpleados,name="BorrarEmpleados")
]
