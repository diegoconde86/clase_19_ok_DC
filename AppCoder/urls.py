from django.urls import path
from .views import *

urlpatterns = [
    path('curso/    ', curso),
    path('carga_datos/', carga),
    path('entrega/<nom_ape>/<documento>/<ocup>',entrega),
    path('entregables/', entregables),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('cursos/', cursos),
    path('', inicio),
]