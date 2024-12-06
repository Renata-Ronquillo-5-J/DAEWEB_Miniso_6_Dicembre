from django.urls import path 
from Clientes_app import views

urlpatterns = [
    path("Clientes",views.inicio_vista,name="Clientes"),
    path("RegistrarClientes/",views.RegistrarClientes,name="RegistrarClientes"),
    path("SeleccionarClientes/<Id_Cliente>",views.SeleccionarClientes,name="SeleccionarClientes"),
    path("EditarClientes/",views.EditarClientes,name="EditarClientes"),
    path("BorrarClientes/<Id_Cliente>",views.BorrarClientes,name="BorrarClientes")
]
