# mi_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('insertar/', views.insertar_datos, name='insertar_datos'),
    path('buscar/', views.buscar_estudiante, name='buscar_estudiante'),
]
