from django.contrib import admin

# Register your models here.
from .models import Receta, Categorias

class RecetaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')#fechas de creación y modificacion de la receta
    list_display = ('nombre','subnombre','author')
    ordering = ('nombre','author')
    search_fields = ('nombre','subnombre','author__username','categorias__nombre')##para crear un buscador y buscar segú  queramos
    date_hierarchy = ('created')#jerarquía de fechas
    list_filter = ('categorias__nombre',)

class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('nombre','descripcion')

admin.site.register(Receta, RecetaAdmin)
admin.site.register(Categorias, CategoriasAdmin)

