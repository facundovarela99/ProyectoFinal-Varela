from django.db import models

# Create your models here.

class yerba(models.Model):
    nombre=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    fecha_vencimiento=models.DateField()
    def __str__(self):
        return self.nombre+" "+self.tipo+" "+str(self.fecha_vencimiento)

class mate(models.Model):
    nombre=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    cantidad_x_caja=models.IntegerField()
    def __str__(self):
        return self.nombre+" "+self.tipo+" "+str(self.cantidad_x_caja)

class proveedores(models.Model):
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
