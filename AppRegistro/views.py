from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, 'AppPrueba/inicio.html', {'mensaje':f'Usuario {username} creado correctamente'})
        else:
            return render(request, 'AppPrueba/register.html', {'formulario':form, 'mensaje':'FORMULARIO INVALIDO'})
    else:
        form=UserRegisterForm()
        return render(request, 'AppPrueba/register.html', {'formulario':form})

def obtenerAvatar(request):
    lista=Avatarr.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/avatarpordefecto.png"
    return imagen

def leerUsuarios(request):
    usuarios=User.objects.all()
    return render (request, 'AppPrueba/leerusuarios.html', {'usuarios':usuarios, 'avatar':obtenerAvatar(request)})