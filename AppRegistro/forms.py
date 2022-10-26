from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')
    email= forms.EmailField
    edad = forms.IntegerField()
    genero = forms.CharField(max_length=50)
    password1 = forms.CharField(label='Ingrese Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'edad', 'genero', 'password1', 'password2']
        help_texts = {k:'' for k in fields}
    
