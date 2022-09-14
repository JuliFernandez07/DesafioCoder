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
            return render(request, "AppGimnasio/Inicio.html")
    else:
        formulario = ProfeFormulario()

    return render(request, "AppGimnasio/profeFormulario.html", {"formulario":formulario})

def alumnoForm(request):
    if request.method == "POST":
        formulario = AlumnoFormulario(request.POST)
        print(formulario)

        if formulario.is_valid:
            info = formulario.cleaned_data
            alumno_1 = alumno(nombre=info["nombre"], apellido=info["apellido"], contacto=info["contacto"], mail=info["mail"])
            alumno_1.save()
            return render(request, "AppGimnasio/Inicio.html")
    else:
        formulario = AlumnoFormulario()

    return render(request, "AppGimnasio/alumnoFormulario.html", {"formulario":formulario})

def buscarprofe(request):
    return render(request, "AppGimnasio/buscarprofe.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.get["nombre"]
        profe = profesor.objects.filter(nombre__icontains=nombre)
        return render (request, "AppGimnasio/resultadoProfe.html", {"profesor":profe, "nombre":nombre})    
    
    else:
        resultado= "No enviaste datos"

    return HttpResponse(resultado)