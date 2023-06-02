from django.db import models
from applications.app_departamento.models import Departamento

# Create your models here.
class Empleado(models.Model):
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
    job = models.CharField('Puesto', max_length=1,choices=JOB_CHOICES)
    #fk
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #mim
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Recursos laborales'
        ordering = ['first_name']
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return str(self.id) +'-'+self.first_name+'-'+self.last_name
    