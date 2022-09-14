from django.contrib import admin

from AppGimnasio.models import abonos, actividades, alumno, profesor

# Register your models here.
admin.site.register(profesor)
admin.site.register(alumno)
admin.site.register(actividades)
admin.site.register(abonos)