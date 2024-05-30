from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# class Estado(models.Model):
#     estado = models.CharField(max_length=50, unique=True)
    
#     def __str__(self) -> str:
#         return self.estado

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")
    fecha_inicio = models.DateField(null=True, blank=True, default=timezone.now)
    fecha_fin = models.DateField(null=True, blank=True, default=timezone.now)
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='proyectos_responsable')
    
    @property
    def avance(self):
        total_tareas = self.related_tareas.count()
        if total_tareas == 0:
            return 0
        tareas_completadas = self.related_tareas.filter(completada=True).count()
        return (tareas_completadas / total_tareas) * 100
    
    def __str__(self) -> str:
        """Representa una instancia del modelo como una cadena de texto"""
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=200)
    completada = models.BooleanField(default=False)
    proyecto = models.ForeignKey(Proyecto, related_name='related_tareas', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre