import re
from turtle import isvisible
from django.http import HttpResponse
from django.template import Context,Template,loader
from django.shortcuts import render
from AppCoder.models import Curso, Familia, Profesor
from AppCoder.forms import CursoForm, ProfeForm

 
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

"""def cursoformulario(request):
    if (request.method == "POST"):
        nombre= request.POST.get("curso")
        comi=curso= request.POST.get("comision")
        curso= Curso(nombre=nombre, comision=comi)
        curso.save()
        return render (request,"AppCoder/inicio.html")  
    
    return render (request,"AppCoder/cursoformulario.html")  VISTA PARA FORMULARIO HTML   """

def cursoformulario(request):  
    if (request.method == "POST"):
        form = CursoForm(request.POST)
        print(form)
        if form.is_valid():
            info=form.cleaned_data
            print(info)
            nombre=info["nombre"]
            comision=info["comision"]
            curso= Curso(nombre=nombre, comision=comision)
            curso.save()
            return render (request,"AppCoder/inicio.html")  
    else:
        form=CursoForm()
    return render(request,"AppCoder/cursoformulario.html",{"formulario":form})

def profeformulario(request):  
    if (request.method == "POST"):
        form = ProfeForm(request.POST)
        print(form)
        if form.is_valid():
            info=form.cleaned_data
            print(info)
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            profesion=info["profesion"]
            profe= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            return render (request,"AppCoder/inicio.html")  
    else:
        form=ProfeForm()
    return render(request,"AppCoder/profeformulario.html",{"formulario":form})

def busquedacomision(request):
    return render(request, "AppCoder/busquedacomision.html")

def buscar(request):
    if request.GET["comision"]:
        comi= request.GET["comision"]
        cursos=Curso.objects.filter(comision=comi)
        return render(request, "AppCoder/resultadosbusqueda.html", {"cursos":cursos})
    else:
        return render(request, "AppCoder/busquedacomision.html", {"error":" No se ingreso ninguna Comision"})

    

 