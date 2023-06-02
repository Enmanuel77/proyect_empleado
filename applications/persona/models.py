from django.db import models
from applications.app_departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) +'-'+self.habilidad    

# Create your models here.
class Persona(models.Model):
    """ Modelo para tabla empleado"""

    JOB_CHOICES = (
        ('0','Jefe'),
        ('1','Asistente'),
        ('2','Auxiliar'),
        ('3','Administrativo'),
    )
    #mc
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('apellidos', max_length=60)
    full_name = models.CharField('Nombres Completos', max_length=120, blank=True)
    job = models.CharField('Puesto', max_length=1,choices=JOB_CHOICES)
    #fk
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #mim
    #avatar = models.ImageField(upload_to='persona',blank=True, null=True)
    #m2m
    habilidades = models.ManyToManyField(Habilidades)
    hoja_Vida = RichTextField()

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['first_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return str(self.id) +'-'+self.first_name+'-'+self.last_name

