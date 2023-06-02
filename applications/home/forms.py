from django import forms
from .models import Prueba

#mf
class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields =('titulo',
                 'subtitulo',
                 'cantidad',
        )
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese texto'
                }
            ),'subtitulo': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese texto'
                }
            ),'cantidad': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese cantidad'
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un valor mayor a 10')

        return cantidad
                    