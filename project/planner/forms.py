from django import forms
from . import models

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = models.Proyecto
        fields = "__all__"

class TareaForm(forms.ModelForm):
    class Meta:
        model = models.Tarea
        fields = "__all__"