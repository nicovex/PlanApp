from django import forms
from django.forms.models import modelformset_factory
from . import models

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = models.Proyecto
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_inicio": forms.DateInput(attrs={"class": "form-control"}),
            "fecha_fin": forms.DateInput(attrs={"class": "form-control"}),
        }

class TareaForm(forms.ModelForm):
    class Meta:
        model = models.Tarea
        fields = "__all__"

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = models.Responsable
        fields = "__all__"
        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }