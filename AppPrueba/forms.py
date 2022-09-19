from django import forms

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