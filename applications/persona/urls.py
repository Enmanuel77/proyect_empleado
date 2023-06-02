from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view(), name='all_empleados'),
    path('listar-by-area/<short_name>', views.ListByAreaEmpleado.as_view(),name='empleados_area'),
    path('listar-empleados-admin/', views.ListEmpleadosAdmin.as_view(), name='empleados_Admin'),
    path('buscar-empleado/', views.ListBykword.as_view()),
    path('listar-habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(),name='empleado_detail'),
    path('agregar-empleado/', views.PersonaCreateView.as_view(),name='empleado_add'),
    path('success/', views.SuccessView.as_view(),name='correcto'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(),name='modificar_empleados'),
    path('up/', views.SuccessView.as_view(), name='modificar_empleado'),
    path('eliminar-empleado/<pk>/', views.EmpleadoDeleteView.as_view(),name='eliminar_empleado'),
    path('delete-empleado/', views.SuccessView.as_view(), name='empleado_eliminado'),
]