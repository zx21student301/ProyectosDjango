from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now 

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True)
    #auto_now_add añade la fecha actual una vez
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    #auto_now añade la fecha cada vez que se guarde o se modifique
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural='categorias'
        ordering=['-created']

    def __str__(self):
        return self.nombre
        
class Receta(models.Model):
    nombre = models.CharField(max_length=255)
    subnombre = models.CharField(max_length=255, null=True)
    imagen = models.ImageField(verbose_name='Foto receta', upload_to='recetario')
    ingredientes = models.TextField(null=True)
    receta = models.TextField(null=True)
    #auto_now_add añade la fecha actual una vez
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    #auto_now añade la fecha cada vez que se guarde o se modifique
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    #PROTECT -> si se borra el autor no se borra la receta
    #CASCADE -> si se borra el autor se borra la receta
    author = models.ForeignKey(User, verbose_name="author", on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria, verbose_name='categorias')

    class Meta:
        verbose_name = 'receta'
        verbose_name_plural='recetas'
        ordering=['-created']

    def __str__(self):
        return self.nombre