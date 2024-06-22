from django.shortcuts import render
from django.http import HttpResponse
from cadastro.models import Cliente, Marca

# Create your views here.
def index(request):
    return render(request, 'index.html') 

def segundo(request):
    return render(request, 'pagina2.html')    

def listarMarcas(request):
    marcas = Marca.objects.order_by('nome')
    return render(request, 'marcas/lista.html',{'marcas': marcas}) 

def listarCliente(request):
    cliente = Cliente.objects.order_by('nome')
    return render(request, 'cliente/lista.html',{'cliente': cliente}) 