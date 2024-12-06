from django.urls import path 
from Venta_app import views

urlpatterns = [
    path("Ventas",views.inicio_vista,name="Ventas"),
    path("RegistrarVentas/",views.RegistrarVentas,name="RegistrarVentas"),
    path("SeleccionarVentas/<Id_Venta>",views.SeleccionarVentas,name="SeleccionarVentas"),
    path("EditarVentas/",views.EditarVentas,name="EditarVentas"),
    path("BorrarVentas/<Id_Venta>",views.BorrarVentas,name="BorrarVentas"),
]
 