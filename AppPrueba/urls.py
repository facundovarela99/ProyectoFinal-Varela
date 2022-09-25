from django.urls import path 
from AppPrueba.views import *

urlpatterns = [
    
    path('', inicio, name = 'inicio'),
    path('yerbas/', yerbasSAPE, name = 'yerbas'),
    path('proveedor/', proveedor, name = 'proveedor'),
    path('mates/', mates, name = 'mates'),
    #yerbas
    path('leeryerbas/', leeryerbas, name = 'leeryerbas'),
    path('eliminarYerba/<id>', eliminarYerba, name = 'eliminarYerba'),
    path('editarYerba/<id>', editarYerba, name= 'editarYerba'),
    #proveedores
    path('leerproveedores/', leerproveedores, name = 'leerproveedores'),
    path('eliminarProveedor/<id>', eliminarProveedor, name = 'eliminarProveedor'),
    #mates
    path('leermates/', leermates, name = 'leermates'),
    path('eliminarMate/<id>', eliminarMate, name = 'eliminarMate'),
]