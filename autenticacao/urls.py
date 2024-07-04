from django.urls import path
from . import views

urlpatterns = [
    path("login", views.logar, name='login'),
    path('sair', views.sair, name='sair'),
    path('resgistro', views.registro, name='registro'),
]
