from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):
    return render (request, 'AppPrueba/inicio.html')

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
            return render (request, 'AppPrueba/inicio.html', {'mensaje':'Yerba Creada!'})
    else:
        form=yerbaForms()
    return render (request, 'AppPrueba/yerbas.html', {'formulario':form})

def proveedor(request):
    if request.method=='POST':
        form=proveedoresForms(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['nombre']
            prov=proveedores(nombre=nombre)
            prov.save()
            return render (request, 'AppPrueba/inicio.html', {'mensaje':'Proveedor creado!'})
    else:
        form=proveedoresForms
    return render (request, 'AppPrueba/proveedor.html', {'formulario':form})

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
            return render (request, 'AppPrueba/inicio.html', {'mensaje':'Mate creado!'})
    else:
        form=mateForms
    return render (request, 'AppPrueba/mate.html', {'formulario':form})
            


















#CBV
# class yerbaCreacion(CreateView):
#     model = yerba
#     success_url = reverse_lazy('yerba_creacion')
#     fields=['nombre', 'tipo', 'fecha_vencimiento']