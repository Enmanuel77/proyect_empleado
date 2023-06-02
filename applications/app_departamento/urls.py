from django.urls import path
from .import views

app_name = 'app_departamento'

urlpatterns = [
    path('new-departamento/', views.NewDepartamentoView.as_view(), name='nuevo_departamento'),
    path('departamentos/', views.DepartamentoListView.as_view(), name='lista_departamento'),
]

