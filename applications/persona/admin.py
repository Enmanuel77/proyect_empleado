from django.contrib import admin
from .models import Persona, Habilidades
# Register your models here.
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )
    ordering = 'id',
    def full_name(self, obj):
        return obj.first_name + ' '+obj.last_name

    search_fields = ('first_name',)
    list_filter = ('job','habilidades', 'departamento')

    #esta opcion solo funciona con una relación muchos a muchos
    filter_horizontal = ('habilidades',)

admin.site.register(Persona, EmpleadoAdmin)