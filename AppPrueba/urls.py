from django.urls import path 
from AppPrueba.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', inicio, name = 'inicio'),
    path('yerbas/', yerbasSAPE, name = 'yerbas'),
    path('proveedor/', proveedor, name = 'proveedor'),
    path('mates/', mates, name = 'mates'),
    
    #yerbas
    path('leeryerbas/', leeryerbas, name = 'leeryerbas'),
    #VBC
    path('yerba/list', YerbasList.as_view(), name = 'yerbas_listar'),
    path('yerba/<pk>', YerbaDetalle.as_view(), name ='yerba_detalle'),
    
    path('eliminarYerba/<id>', eliminarYerba, name = 'eliminarYerba'),
    path('editarYerba/<id>', editarYerba, name= 'editarYerba'),
    
    #proveedores
    path('leerproveedores/', leerproveedores, name = 'leerproveedores'),
    path('eliminarProveedor/<id>', eliminarProveedor, name = 'eliminarProveedor'),
    
    #mates
    path('leermates/', leermates, name = 'leermates'),
    path('eliminarMate/<id>', eliminarMate, name = 'eliminarMate'),
    #VBC
     path('mate/list', MatesList.as_view(), name = 'mates_listar'),

    
    #logout
    path('logout/', LogoutView.as_view(template_name='AppPrueba/logout.html'), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    
    #avatar
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
   
]