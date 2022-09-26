from django.shortcuts import render
from .models import *
from AppPrueba.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def inicio(request):
    return render (request, 'AppPrueba/inicio.html')


#####YERBA#####
def yerbasSAPE(request):
    if request.method=='POST':
        form=yerbaForms(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['nombre']
            tipo=info['tipo']
            fecha_vencimiento=info['fecha_vencimiento']
            yerbilla=yerba(nombre=nombre, tipo=tipo, fecha_vencimiento=fecha_vencimiento)
            yerbilla.save()
            yerbillas=yerba.objects.all()
            return render (request, 'AppPrueba/leeryerbas.html', {'yerbillas':yerbillas})
    else:
        form=yerbaForms()
    return render (request, 'AppPrueba/yerbas.html', {'formulario':form})

def leeryerbas(request):
    yerbillas=yerba.objects.all()
    return render (request, 'AppPrueba/leeryerbas.html', {'yerbillas':yerbillas})

def editarYerba(request, id):
    yerbilla=yerba.objects.get(id=id) #playground avanzado part 1 CRUD (38:02)
    if request.method=='POST':
        form=yerbaForms(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            yerbilla.nombre=info['nombre']
            yerbilla.tipo=info['tipo']
            yerbilla.fecha_vencimiento=info['fecha_vencimiento']
            yerbilla.save()
            yerbillas=yerba.objects.all()
            return render(request, 'AppPrueba/leeryerbas.html', {'yerbillas':yerbillas})
    else:
        form=yerbaForms(initial={'nombre':yerbilla.nombre, 'tipo':yerbilla.tipo, 'fecha_vencimiento':yerbilla.fecha_vencimiento})
        return render(request, 'AppPrueba/editarYerba.html', {'formulario':form, 'yerbilla':yerbilla})


def eliminarYerba(request, id):
    yerbilla=yerba.objects.get(id=id)
    yerbilla.delete()
    yerbillas=yerba.objects.all()
    return render(request, 'AppPrueba/leeryerbas.html', {'yerbillas':yerbillas})
#####YERBA#####

#####PROVEEDOR#####
def proveedor(request):
    if request.method=='POST':
        form=proveedoresForms(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['nombre']
            prov=proveedores(nombre=nombre)
            prov.save()
            provs=proveedores.objects.all()
            return render (request, 'AppPrueba/leerproveedores.html', {'provs':provs})
    else:
        form=proveedoresForms
    return render (request, 'AppPrueba/proveedor.html', {'formulario':form})

def leerproveedores(request):
    provs=proveedores.objects.all()
    return render (request, 'AppPrueba/leerproveedores.html', {'provs':provs})

def eliminarProveedor(request, id):
    proveedor=proveedores.objects.get(id=id)
    proveedor.delete()
    provs=proveedores.objects.all()
    return render(request, 'AppPrueba/leerproveedores.html', {'provs':provs})
#####PROVEEDOR#####

#####MATES#####
def mates(request):
    if request.method=='POST':
        form=mateForms(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['nombre']
            tipo=info['tipo']
            cantidad_x_caja=info['cantidad_x_caja']
            mat=mate(nombre=nombre, tipo=tipo, cantidad_x_caja=cantidad_x_caja)
            mat.save()
            mats=mate.objects.all()
            return render (request, 'AppPrueba/leermates.html', {'mats':mats})
    else:
        form=mateForms
    return render (request, 'AppPrueba/mate.html', {'formulario':form})

def leermates(request):
    mats=mate.objects.all()
    return render(request, 'AppPrueba/leermates.html', {'mats':mats})

def eliminarMate(request, id):
    mat=mate.objects.get(id=id)
    mat.delete()
    mats=mate.objects.all()
    return render(request, 'AppPrueba/leermates.html', {'mats':mats})
#####MATES#####

#LOGIN-LOGOUT-REGISTER
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





















#CBV
# class yerbaCreacion(CreateView):
#     model = yerba
#     success_url = reverse_lazy('yerba_creacion')
#     fields=['nombre', 'tipo', 'fecha_vencimiento']