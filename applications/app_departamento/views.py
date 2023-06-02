from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from applications.persona.models import Persona
from .models import Departamento
from . forms import NewDepartamentoForm
# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "app_departamento/lista.html"
    context_object_name ='departamentos'


class NewDepartamentoView(FormView):
    template_name = 'app_departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url ='/'

    def form_valid(self, form):
        print('***esto es parte del form valid***')

        depa = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['short_name']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']

        Persona.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = 1,
            departamento = depa

        )

        return super(NewDepartamentoView, self).form_valid(form)

        
