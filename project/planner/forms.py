from django import forms
from django.forms.models import modelformset_factory
from . import models

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = models.Proyecto
        fields = "__all__"

class TareaForm(forms.ModelForm):
    class Meta:
        model = models.Tarea
        fields = "__all__"

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = models.Responsable
        fields = "__all__"