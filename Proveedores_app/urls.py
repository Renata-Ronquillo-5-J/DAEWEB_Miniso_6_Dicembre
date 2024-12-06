from django.urls import path 
from Proveedores_app import views

urlpatterns = [
    path("Proveedores",views.inicio_vista,name="Proveedores"),
    path("RegistrarProveedores/",views.RegistrarProveedores,name="RegistrarProveedores"),
    path("SeleccionarProveedores/<Id_Proveedor>",views.SeleccionarProveedores,name="SeleccionarProveedores"),
    path("EditarProveedores/",views.EditarProveedores,name="EditarProveedores"),
    path("BorrarProveedores/<Id_Proveedor>",views.BorrarProveedores,name="BorrarProveedores"),
]
