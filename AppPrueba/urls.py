from django.urls import path 
from AppPrueba.views import *

urlpatterns = [
    
    path('', inicio, name = 'inicio'),
    path('yerbas/', yerbasSAPE, name = 'yerbas'),
    path('proveedor/', proveedor, name = 'proveedor'),
    path('mates/', mates, name = 'mates'),
    path('leeryerbas/', leeryerbas, name = 'leeryerbas'),
    path('eliminarYerba/<id>', eliminarYerba, name = 'eliminarYerba'),
    path('editarYerba/<id>', editarYerba, name= 'editarYerba'),
    path('leerproveedores/', leeryerbas, name = 'leeryerbas'),
    path('eliminarProveedor/', eliminarProveedor, name = 'elimnarProveedor'),
    
    


]