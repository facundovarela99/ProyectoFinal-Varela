from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

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
            return render (request, 'AppPrueba/leerproveedor.html', {'mensaje':'Proveedor creado!'})
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
    return render(request, 'AppPrueba/leeryerbas.html', {'provs':provs})





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