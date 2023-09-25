from django import forms


class VendedorFormulario(forms.Form):
    #Especificar los campos
    documentoVendedor = forms.IntegerField()
    nombreVendedor = forms.CharField(max_length=20)
    apellidoVendedor = forms.CharField(max_length=20)
    
class VentaFormulario(forms.Form):
    #Especificar los campos
    fechaVenta = forms.DateField()
    montoVenta = forms.FloatField()
    documentoVendedor = forms.IntegerField()

class ClienteFormulario(forms.Form):
    #Especificar los campos
    nombreCliente = forms.CharField(max_length=20)
    apellidoCliente = forms.CharField(max_length=20)
    numeroCliente = forms.IntegerField()