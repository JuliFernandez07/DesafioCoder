from django.db import models

# Create your models here.
class profesor(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    actividad = models.CharField(max_length=15)
    contacto = models.IntegerField()


class alumno(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    contacto = models.IntegerField()
    mail = models.EmailField()

class actividades(models.Model):
    nombre = models.CharField(max_length=15)

class abonos(models.Model):
    precios = models.IntegerField
    

