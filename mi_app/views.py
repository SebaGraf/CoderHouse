# mi_app/views.py
from django.shortcuts import render, redirect
from .forms import EstudianteForm, CursoForm, InscripcionForm, BuscarForm

def insertar_datos(request):
    if request.method == 'POST':
        estudiante_form = EstudianteForm(request.POST)
        curso_form = CursoForm(request.POST)
        inscripcion_form = InscripcionForm(request.POST)
        if estudiante_form.is_valid() and curso_form.is_valid() and inscripcion_form.is_valid():
            estudiante_form.save()
            curso_form.save()
            inscripcion_form.save()
            return redirect('index')
    else:
        estudiante_form = EstudianteForm()
        curso_form = CursoForm()
        inscripcion_form = InscripcionForm()

    return render(request, 'insertar_datos.html', {
        'estudiante_form': estudiante_form,
        'curso_form': curso_form,
        'inscripcion_form': inscripcion_form
    })

def buscar_estudiante(request):
    form = BuscarForm(request.GET)
    estudiantes = []
    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        estudiantes = Estudiante.objects.filter(nombre__icontains=nombre)

    return render(request, 'buscar_estudiante.html', {'form': form, 'estudiantes': estudiantes})
