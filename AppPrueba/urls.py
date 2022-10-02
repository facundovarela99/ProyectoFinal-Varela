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
    path('eliminarYerba/<id>', eliminarYerba, name = 'eliminarYerba'),
    path('editarYerba/<id>', editarYerba, name= 'editarYerba'),
    #proveedores
    path('leerproveedores/', leerproveedores, name = 'leerproveedores'),
    path('eliminarProveedor/<id>', eliminarProveedor, name = 'eliminarProveedor'),
    #mates
    path('leermates/', leermates, name = 'leermates'),
    path('eliminarMate/<id>', eliminarMate, name = 'eliminarMate'),
    #login-logout-register
    path('login/', login_request, name = 'login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='AppPrueba/logout.html'), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
]