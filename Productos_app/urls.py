from django.urls import path 
from Productos_app import views

urlpatterns = [
    path("Productos",views.inicio_vista,name="Productos"),
    path("RegistrarProductos/",views.RegistrarProductos,name="RegistrarProductos"),
    path("SeleccionarProductos/<Id_Producto>",views.SeleccionarProductos,name="SeleccionarProductos"),
    path("EditarProducto/",views.EditarProducto,name="EditarProducto"),
    path("BorrarProductos/<Id_Producto>",views.BorrarProductos,name="BorrarProductos")
]
