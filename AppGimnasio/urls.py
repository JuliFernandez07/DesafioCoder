from django.urls import path
from AppGimnasio.views import clases, inicio, profesores, alumnos
from . import views
urlpatterns = [
    path('clases/', views.clases),
    path("profesores/", views.profesores),
    path("alumnos/", views.alumnos),
    path ("inicio/", views.inicio)
]