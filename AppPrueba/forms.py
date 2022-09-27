from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class yerbaForms(forms.Form):
    nombre=forms.CharField(max_length=50)
    tipo=forms.CharField(max_length=50)
    fecha_vencimiento=forms.DateField()

class mateForms(forms.Form):
    nombre=forms.CharField(max_length=50)
    tipo=forms.CharField(max_length=50)
    cantidad_x_caja=forms.IntegerField()

class proveedoresForms(forms.Form):
    nombre=forms.CharField(max_length=50)

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField
    password1 = forms.CharField(label='Ingrese Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

class UserEditForm(UserCreationForm):
    first_name=forms.CharField(label='Modificar nombre')
    last_name=forms.CharField(label='Modificar apellido')
    email= forms.EmailField
    password1 = forms.CharField(label='Ingrese Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

