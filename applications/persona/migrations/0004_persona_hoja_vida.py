# Generated by Django 4.2.1 on 2023-05-09 22:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_alter_persona_unique_together_persona_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='hoja_Vida',
            field=ckeditor.fields.RichTextField(default='texto'),
            preserve_default=False,
        ),
    ]
