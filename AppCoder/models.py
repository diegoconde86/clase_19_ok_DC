from distutils.archive_util import make_zipfile
from pickle import TRUE
from django.db import models

class Curso(models.Model):

    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()

class Estudiante(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    
class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)
    
class Entregable(models.Model):
    nombre= models.CharField(max_length=50)
    fecha_entrega= models.DateField()
    entregado= models.BooleanField()

class Familia(models.Model):
    nombre_apellido= models.CharField(max_length=50)
    dni= models.IntegerField()
    fecha_actualizacion= models.DateField(auto_now_add=TRUE)
    ocupacion=models.CharField(max_length=50)
    

# Create your models here.
