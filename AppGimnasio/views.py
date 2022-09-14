from django.http import HttpResponse
from django.template import Template
from AppGimnasio.forms import AlumnoFormulario, ProfeFormulario
from AppGimnasio.models import *
from django.shortcuts import render
# Create your views here.

def clases(request):  
    return render(request, "AppGimnasio/Clases.html")

def profesores(request):

    return render(request, "AppGimnasio/Profesores.html")

def alumnos(request):

    return render(request, "AppGimnasio/Alumnos.html")

def inicio(request):
    return render(request, "AppGimnasio/Inicio.html")

def abono(request):
    return render(request, "AppGimnasio/Abonos.html")

def profeForm(request):
    if request.method == "POST":
        formulario = ProfeFormulario(request.POST)
        print(formulario)

        if formulario.is_valid:
            info = formulario.cleaned_data
            profe = profesor(nombre=info["nombre"], apellido=info["apellido"], actividad=info["actividad"], contacto=info["contacto"])
            profe.save()
            return render("AppGimnasio/Inicio.html")
    else:
        formulario = ProfeFormulario()

    return render(request, "AppGimnasio/profeFormulario.html", {"formulario":formulario})

def alumnoForm(request):
    if request.method == "POST":
        formulario = AlumnoFormulario(request.POST)
        print(formulario)

        if formulario.is_valid:
            info = formulario.cleaned_data
            profe = alumno(nombre=info["nombre"], apellido=info["apellido"], contacto=info["contacto"], email=info["email"])
            profe.save()
            return render("AppGimnasio/Inicio.html")
    else:
        formulario = AlumnoFormulario()

    return render(request, "AppGimnasio/alumnoFormulario.html", {"formulario":formulario})