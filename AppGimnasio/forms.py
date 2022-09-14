from django import forms

class ProfeFormulario(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)
    actividad = forms.CharField(max_length=15)
    contacto = forms.IntegerField()

class AlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)
    contacto = forms.IntegerField()
    mail = forms.EmailField()
    