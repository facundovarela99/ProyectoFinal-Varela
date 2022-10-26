from django.urls import path 
from AppRegistro.views import *

urlpatterns = [

path('register/', register, name='register'),
path('leerUsuarios/', leerUsuarios, name='leerUsuarios'),
]