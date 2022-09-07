from django.urls import path
from AppGimnasio.views import clases, inicio, profesores, alumnos

urlpatterns = [
    path('clases/', clases),
    path("profesores/", profesores),
    path("alumnos/", alumnos),
    path ("inicio/", inicio)
]