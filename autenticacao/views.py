from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import messages

from autenticacao.forms import NovoUsarioForm

# Create your views here.

def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            senha = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=senha)  

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Usuário Inválido') 
        else:
                messages.error(request, 'Usuário Inválido')         

        
    form = AuthenticationForm()
    return render (request, 'login.html', {'form': form})

def sair(request):
    logout(request)   
    return redirect('index')


def registro(request):
    if request.method == 'POST':
        form = NovoUsarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Usuário registrado com sucesso')
            return redirect('index')
        messages.error(request, 'Erro ao cadastrar o usuário')   

    form = NovoUsarioForm()
    return render(request, 'registro.html', {'form': form})    