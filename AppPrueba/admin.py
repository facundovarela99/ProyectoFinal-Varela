from django.contrib import admin
from .models import *
from .forms import *
from AppLogin.models import Avata
from AppRegistro.models import Avatarr
# Register your models here.
admin.site.register(yerba)
admin.site.register(mate)
admin.site.register(proveedores)
admin.site.register(Avatar)
#AppLogin
admin.site.register(Avata)
#AppRegistro
admin.site.register(Avatarr)
