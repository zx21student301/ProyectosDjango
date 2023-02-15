from django.db import models

# Create your models here.
class Propositos(models.Model):
    proposito = models.CharField(max_length=255)
    fechaObjetivo = models.DateField()
    conseguido = models.BooleanField()
    fechaConseguido = models.DateTimeField(null=True)