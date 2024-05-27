from django.db import models
from django.utils import timezone

# Create your models here.
class Estado(models.Model):
    estado = models.CharField(max_length=50, unique=True)
    
    def __str__(self) -> str:
        return self.estado

class Tarea(models.Model):
    nombre = models.CharField(max_length=200)
    # responsable = models.OneToOneField()
    estado_id = models.ForeignKey(Estado, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")
    fecha_inicio = models.DateField(null=True, blank=True, default=timezone.now)
    fecha_fin = models.DateField(null=True, blank=True, default=timezone.now)
    tareas = models.ManyToManyField(Tarea)
    
    def __str__(self) -> str:
        """Representa una instancia del modelo como una cadena de texto"""
        return self.nombre