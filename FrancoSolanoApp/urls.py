from django.urls import path
from FrancoSolanoApp import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('vendedores', views.vendedores, name="Vendedores"),
    path('vendedores_formulario', views.vendedores_formulario, name="vendedores_formulario"),
    path('ventas_formulario', views.venta_formulario, name="ventas_formulario"),
    path('clientes', views.cliente_formulario, name="clientes_formulario"),
    path('buscar_ventas', views.buscar_ventas, name="buscar_ventas"),
    path('buscar', views.buscar,name="buscar"),
]


