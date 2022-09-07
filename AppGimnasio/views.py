from django.http import HttpResponse
from django.template import Template
from AppGimnasio.models import *
from django.shortcuts import render
# Create your views here.

def clases(request):   
    return render(request, "C:/Users/Julián/Desktop/GymHouse/AppGimnasio/Templates/Clases.html")

def profesores(request):

    return render(request, "C:/Users/Julián/Desktop/GymHouse/AppGimnasio/Templates/Profesores.html")

def alumnos(request):

    return render(request, "C:/Users/Julián/Desktop/GymHouse/AppGimnasio/Templates/Alumnos.html")

def inicio(request):
    return render(request, "C:/Users/Julián/Desktop/GymHouse/AppGimnasio/Templates/Inicio.html")
