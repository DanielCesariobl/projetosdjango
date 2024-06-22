from django.urls import path
from . import views
urlpatterns =[
    path('', views.index, name='index'),
    path('/segundo', views.segundo, name = 'segundo'),
    
    #Marcas
    path('/listar_marcas', views.listarMarcas,
    name= 'listar_marcas'),

    #cliente
    path('/listar_cliente', views.listarCliente,
    name='listar_cliente'),

]