from django.urls import path 
from AppPrueba.views import *

urlpatterns = [
    
    path('', inicio, name = 'inicio'),
    path('yerbas/', yerbasSAPE, name = 'yerbas'),
    path('proveedor/', proveedor, name = 'proveedor'),
    path('mates/', mates, name = 'mates'),

]