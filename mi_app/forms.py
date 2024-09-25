# mi_app/forms.py
from django import forms
from .models import Estudiante, Curso, Inscripcion

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'email']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'descripcion']

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['estudiante', 'curso', 'fecha_inscripcion']

class BuscarForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)