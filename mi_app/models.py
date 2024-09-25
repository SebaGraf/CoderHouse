from django.db import models

# Create your models here.
# mi_app/models.py
from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.titulo

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()

    def __str__(self):
        return f'{self.estudiante.nombre} - {self.curso.titulo}'
