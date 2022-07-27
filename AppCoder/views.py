import re
from turtle import isvisible
from django.http import HttpResponse
from django.template import Context,Template,loader
from django.shortcuts import render
from django.urls import is_valid_path
from AppCoder.models import Curso, Familia, Profesor
from AppCoder.forms import CursoForm, ProfeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

 
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


def leerprofesores(request):
    profesores= Profesor.objects.all()
    contexto={"profesores":profesores}
    return render(request, "AppCoder/leerprofesores.html",contexto)

def eliminarprofesor(request, nombre_profesor):
    profe= Profesor.objects.get(nombre=nombre_profesor)
    profe.delete()
    profesores= Profesor.objects.all()
    contexto={"profesores":profesores}
    return render(request, "AppCoder/leerprofesores.html",contexto)

def editarprofesor(request,nombre_profesor):
    profe= Profesor.objects.get(nombre=nombre_profesor)
    if request.method == "POST":
        form = ProfeForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            profe.nombre= info["nombre"]
            profe.apellido= info["apellido"]
            profe.email= info["email"]
            profe.profesion= info["profesion"]
            profe.save()
            return render(request,"AppCoder/inicio.html")
    else:
        form= ProfeForm(initial={"nombre":profe.nombre, "apellido":profe.apellido, "email":profe.email, "profesion":profe.profesion})
    return render(request, "AppCoder/editarprofesor.html",{"formulario":form, "nombre_profesor":nombre_profesor})
#-------------------------LOGIN---------------------------------#

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid:
            usu= request.POST['username']
            contra= request.POST['password']
            print("HOLA")
            usuario=authenticate(username=usu,password=contra)
          
            if usuario is not None:
                login(request,usuario)
                return render(request,"AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}."})
            else:
                print(usu)
                print(contra)
                return render(request,"AppCoder/login.html", {"mensaje":"Error, datos incorrectos."})
        else:
                return render(request,"AppCoder/login.html", {"mensaje":"Error, Formulario erroneo."})
    form=AuthenticationForm()
    return render(request,"AppCoder/login.html", {'form':form})
        