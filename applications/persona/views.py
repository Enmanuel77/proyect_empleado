from django.shortcuts import render
from django.urls import reverse_lazy

# 1.-Lista todos los empleados de la empresa
from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView,
)
#models
from .models import Persona
#forms
from .forms import PersonaForm

class InicioView(TemplateView):
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 5

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Persona.objects.filter(
            full_name__icontains = palabra_clave
        )
        return lista


# 2.-Lista todos los empleados que pertenecen a un area de la empresa
class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['short_name']
        lista = Persona.objects.filter(
        departamento__short_name= area
    )
        return lista


class ListEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 8
    context_object_name = 'empleados'
    model = Persona
    ordering = 'id'
    

# 4.-Listar todos los empleados por palabra clave
class ListBykword(ListView):
    template_name = 'persona/by_kword.html'
    #redefinir el nombre con el que se accedera a la lista resultado
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Persona.objects.filter(
            first_name = palabra_clave
        )
        return lista

# 5.-Listar habilidades de un empleado
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        pword = self.request.GET.get('word','')
        empleado = Persona.objects.get(id=pword)
        return empleado.habilidades.all()


#detail
class EmpleadoDetailView(DetailView):
    model = Persona
    template_name = "persona/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class PersonaCreateView(CreateView):
    model = Persona
    template_name = "persona/add.html"
    form_class = PersonaForm
    success_url = reverse_lazy('persona_app:empleados_Admin')

    def form_valid(self, form):
        #logica del proceso
        persona = form.save(commit=False)
        persona.full_name = persona.first_name+' '+persona.last_name
        persona.save()
        return super(PersonaCreateView, self).form_valid(form)
        

class SuccessView(TemplateView):
    template_name = "persona/up.html"


class EmpleadoUpdateView(UpdateView):
    model = Persona
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'hoja_Vida',
    ]
    success_url = reverse_lazy('persona_app:empleados_Admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('***metodo post***')
        print('***metodo***post***')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        #logica del proceso
        print('***metodo form_valid***')
        print('***metodo form_valid***')
        return super(EmpleadoUpdateView, self).form_valid(form)


class SuccessView(TemplateView):
    template_name = "persona/delete-empleado.html"


class EmpleadoDeleteView(DeleteView):
    model = Persona
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_Admin')   

