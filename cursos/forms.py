from django import forms
from .models import Cursos
from django.forms.widgets import CheckboxInput 
class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        # Especifica los campos que quieres incluir en el formulario
        # Excluye 'id', 'created', 'updated' ya que Django los maneja automáticamente
        fields = ['nombre', 'descripcion', 'image', 'estatus', 'precio', 'duracion', 'fecha_inicio']
        widgets = {
            'estatus': CheckboxInput(attrs={'class': 'form-check-input'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'duracion': forms.NumberInput(attrs={'class': 'form-control'}),
        }
