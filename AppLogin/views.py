from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from AppRegistro.models import Avatarr

# Create your views here.

def login_request(request):
    if request.method=='POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST['username']
            clave=request.POST['password']
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'AppPrueba/inicio.html', {'mensaje':f'Bienvenido {usuario}'})
            else:
                return render(request, 'AppPrueba/login.html', {'formulario':form, 'mensaje':f'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'AppPrueba/login.html', {'formulario':form, 'mensaje':f'Usuario o contraseña incorrectos'})
    else:
        form=AuthenticationForm()
        return render(request, 'AppPrueba/login.html', {'formulario':form})

def obtenerAvatar(request):
    lista=Avatarr.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/avatarpordefecto.png"
    return imagen