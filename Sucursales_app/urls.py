from django.urls import path 
from Sucursales_app import views

urlpatterns = [
    path("Sucursales",views.inicio_vista,name="Sucursales"),
    path("RegistrarSucursales/",views.RegistrarSucursales,name="RegistrarSucursales"),
    path("SeleccionarSucursales/<Id_Sucursal>",views.SeleccionarSucursales,name="SeleccionarSucursales"),
    path("EditarSucursales/",views.EditarSucursales,name="EditarSucursales"),
    path("BorrarSucursales/<Id_Sucursal>",views.BorrarSucursales,name="BorrarSucursales"),
]
 