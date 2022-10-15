from django.urls import path
from .views import *

urlpatterns = [

path('dm/<str:username>', mensajes_privados, name='mensajes_privados'),
]