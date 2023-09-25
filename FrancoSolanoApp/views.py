from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from FrancoSolanoApp.models import *
from FrancoSolanoApp.forms import VendedorFormulario, VentaFormulario, ClienteFormulario

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def vendedores(request):
    return render(request, "vendedores.html")

# Agregar vendedor
def vendedores_formulario(request):
    if request.method == 'POST':

        FormVendedor = VendedorFormulario(request.POST)

        print(FormVendedor)

        if FormVendedor.is_valid:

            informacion = FormVendedor.cleaned_data

            vendedor_1 = vendedor(nombre=informacion['nombreVendedor'], apellido=informacion['apellidoVendedor'], numero_empleado=informacion['documentoVendedor']) 
            vendedor_1.save()
            print(vendedor_1)
            return render(request, "vendedores.html") 

      
    return render(request, "vendedores_formulario.html")

# Agregar venta
def venta_formulario(request):
    if request.method == 'POST':

        FormVenta = VentaFormulario(request.POST)

        print(FormVenta)

        if FormVenta.is_valid:

            informacion = FormVenta.cleaned_data

            venta_1= venta(fecha=informacion['fechaVenta'], monto=informacion['montoVenta'], numero_vendedor=informacion['documentoVendedor']) 
            venta_1.save()
            
            return render(request, "inicio.html") 

      
    return render(request, "ventas_formulario.html")

# Agregar cliente
def cliente_formulario(request):
    if request.method == 'POST':

        FormCliente = ClienteFormulario(request.POST)

        print(FormCliente)

        if FormCliente.is_valid:

            informacion = FormCliente.cleaned_data

            venta_1= cliente(nombre=informacion['nombreCliente'], apellid=informacion['apellidoCliente'], numero_cliente=informacion['numeroCliente']) 
            venta_1.save()
            
            return render(request, "inicio.html") 

      
    return render(request, "clientes_formulario.html")

def buscar_ventas(request):

    return render(request, "buscar_ventas.html")

def buscar(request):
    if request.GET['documento']:
        id_vendedor = request.GET['documento']
        ventas = venta.objects.filter(numero_vendedor__icontains=id_vendedor)
        return render(request,'vendedores.html',{'Numero vendedor':id_vendedor,'ventas':ventas})
    else:
        return HttpResponse("No hay datos")

    

    