from django.db import models

# Create your models here.
class Cafe(models.Model):
    nombre= models.CharField(max_length=255)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    imagen_red = models.CharField(max_length=2999)
    