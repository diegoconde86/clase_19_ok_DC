from django.urls import path
from .views import *

urlpatterns = [
    path('curso/    ', curso, name='curso'),
    path('carga_datos/', carga),
    path('entrega/<nom_ape>/<documento>/<ocup>',entrega),
    path('entregables/', entregables, name='entregables'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('profesores/', profesores, name= 'profesores'),
    path('cursos/', cursos, name='cursos'),
    path('cursoformulario/', cursoformulario, name='cursoformulario'),
    path('profeformulario/', profeformulario, name='profeformulario'),
    path('busquedacomision/', busquedacomision, name='busquedacomision'),
    path('buscar/', buscar, name='buscar'),
    path('', inicio, name ='inicio'),
]