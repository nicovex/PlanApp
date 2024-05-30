from django.urls import path
from . import views

app_name = "planner"

# Proyecto
urlpatterns = [
    path("", views.home, name="home"),
    path("proyecto/create/", views.ProyectoCreate.as_view(), name="proyecto_create"),
    path("proyecto/list/", views.ProyectoList.as_view(), name="proyecto_list"),
    path("proyecto/detail/<int:pk>", views.ProyectoDetail.as_view(), name="proyecto_detail"),
    path("proyecto/update/<int:pk>", views.ProyectoUpdate.as_view(), name="proyecto_update"),
    path("proyecto/delete/<int:pk>", views.ProyectoDelete.as_view(), name="proyecto_delete"),
]

# Tareas
urlpatterns += [
    path("tarea/list/", views.TareaList.as_view(), name="tarea_list"),
    path("tarea/create/", views.TareaCreate.as_view(), name="tarea_create"),
    path("tarea/detail/<int:pk>", views.TareaDetail.as_view(), name="tarea_detail"),
    path("tarea/update/<int:pk>", views.TareaUpdate.as_view(), name="tarea_update"),
    path("tarea/delete/<int:pk>", views.TareaDelete.as_view(), name="tarea_delete"),
]

urlpatterns += [
    path("responsable/", views.ResponsableCreate.as_view(), name="responsable"),]