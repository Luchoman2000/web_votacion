from django.db import models

# Create your models here.
class Imagen(models.Model):
    imagen_original = models.ImageField(upload_to='raw_images/')
    imagen_procesada = models.ImageField(upload_to='processed_images/',null=True,blank=True)