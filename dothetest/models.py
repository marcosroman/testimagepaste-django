from django.db import models

# Create your models here.
class Modelo(models.Model):
    texto=models.TextField()
    imagen=models.ImageField()
