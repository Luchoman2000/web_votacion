from django.db import models

# Create your models here.
class Imagen(models.Model):
    imagen_original = models.ImageField(upload_to='raw_images/')
    imagen_procesada = models.ImageField(upload_to='processed_images/',null=True,blank=True)

class Junta(models.Model):
    junta = models.CharField(max_length=100)
    provincia = models.CharField(max_length=200)
    canton = models.CharField(max_length=200)
    parroquia = models.CharField(max_length=200)
    zona = models.CharField(max_length=200)
    circuncripcion = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    
class Acta(models.Model):
    junta = models.ForeignKey(Junta, on_delete=models.DO_NOTHING)
    casillero = models.CharField(max_length=100)
    tot_vacio = models.CharField(max_length=100)
    tot_nulo = models.CharField(max_length=100)
    tot_si = models.CharField(max_length=100)
    tot_no = models.CharField(max_length=100)
    imagen_path = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)


    