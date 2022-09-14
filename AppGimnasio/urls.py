from django.urls import path
from AppGimnasio.views import abono, clases, inicio, profesores, alumnos
from . import views
urlpatterns = [
    path('clases/', views.clases, name="clases"),
    path("profesores/", views.profesores, name="profesores"),
    path("alumnos/", views.alumnos, name="alumnos"),
    path ("inicio/", views.inicio, name="inicio"),
    path("abonos/", views.abono, name="abonos"),
    path("profeFormulario/", views.profeForm, name="profeFormulario"),
    path("alumnoFormulario/", views.alumnoForm, name="alumnoFormulario"),
    path("buscarprofe/", views.buscarprofe, name="buscarprofe"),
    path("buscar/", views.buscar)
]