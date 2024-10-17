from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Usuarios
from .forms import UsuarioForm

def salvarUsuario(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)

        if formulario.is_valid():
            usuario = formulario.save(commit=False)
            usuario.senha = make_password(usuario.senha)
            usuario.save()
            
            return render(request, 'formcad.html')
    
    return render(request, 'formcad.html')

