from django.http import HttpResponse
from django.template import Context,Template,loader
from django.shortcuts import render
from AppCoder.models import Curso, Familia

 
def curso(self):
    curso= Curso(nombre="Django", comision=1234)
    curso.save()
    texto= f"curso creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)

# Create your views here.

def entrega(self, nom_ape, documento, ocup):
    entrega= Familia(nombre_apellido=nom_ape, dni=documento, fecha_actualizacion=1, ocupacion=ocup)
    entrega.save()
    texto= f"Se ingreso el registro de {entrega.nombre_apellido} DNI: {entrega.dni} fecha_nacimiento: {entrega.fecha_actualizacion} ocupacion {entrega.ocupacion}."
    return HttpResponse(texto)

def carga(self):
    
    plantilla=loader.get_template('template1.html')
    documento=plantilla.render()
    return HttpResponse(documento)

def inicio(request):
    return render (request,"AppCoder/inicio.html")

def cursos(request):
   return render (request,"AppCoder/cursos.html")  

def profesores(request):
    return render (request,"AppCoder/profesores.html")

def estudiantes(request):
    return render (request,"AppCoder/estudiantes.html")

def entregables(request):
   return render (request,"AppCoder/entregables.html")     