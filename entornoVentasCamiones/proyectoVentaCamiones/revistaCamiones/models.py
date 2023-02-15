from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorias(models.Model):
    nombre  = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')    

    class Meta:
        verbose_name='categoria'
        verbose_name_plural="categorias"
        ordering=['-created']

    def __str__(self):
        return self.nombre

class Camion (models.Model):
    marca = models.CharField(max_length=200)
    modelo  = models.CharField(max_length=200,null=True)
    imagen = models.ImageField(verbose_name='foto camion',upload_to='revistaCamiones')
    descripcion = models.TextField(null=True)
    precio = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación ')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')
    author = models.ForeignKey(User,verbose_name='autor',on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categorias,verbose_name="categorias")

    class Meta:
        verbose_name='camion'
        verbose_name_plural="camiones"
        ordering=['-created']

    def __str__(self):
        return self.marca