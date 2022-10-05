from django.urls import path 
from AppLogin.views import *

urlpatterns = [

path('login/', login_request, name = 'login'),
]