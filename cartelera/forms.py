from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['id_pelicula', 'titulo', 'duracion', 'genero', 'clasificacion']
