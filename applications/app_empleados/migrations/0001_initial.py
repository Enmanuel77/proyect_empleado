# Generated by Django 4.2.1 on 2023-05-08 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=60, verbose_name='apellidos')),
                ('job', models.CharField(choices=[('0', 'Jefe'), ('1', 'Asistente'), ('2', 'Auxiliar'), ('3', 'Administrativo')], max_length=1, verbose_name='Puesto')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_departamento.departamento')),
            ],
        ),
    ]
