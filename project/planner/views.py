# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models


def home(request):
    return render(request, "planner/index.html")


# *** TareaCATEOGORIA

# LIST
# def Proyecto_list(request):
#     consulta = request.GET.get("consulta", None)
#     if consulta:
#         print(consulta)
#         query = models.Proyecto.objects.filter(nombre__icontains=consulta)
#     else:
#         query = models.Proyecto.objects.all()
#     context = {"Tareas": query}
#     return render(request, "Tarea/Proyecto_list.html", context)


class ProyectoList(ListView):
    model = models.Proyecto

    # context_object_name = "Tareas"
    # template_name = "Tarea/Proyecto___list.html"

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Proyecto.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Proyecto.objects.all()
        return object_list

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     consulta = self.request.GET.get("consulta")
    #     if consulta:
    #         queryset = queryset.filter(Q(nombre__icontains=consulta) | Q(descripcion__icontains=consulta))
    #     return queryset


# CREATE
# def Proyecto_create(request):
#     if request.method == "POST":
#         form = forms.ProyectoForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect("Tarea:home")
#     else:  # request.method == "GET"
#         form = forms.ProyectoForm()
#     return render(request, "Tarea/Proyecto_create.html", context={"form": form})


class ProyectoCreate(CreateView):
    model = models.Proyecto
    form_class = forms.ProyectoForm
    success_url = reverse_lazy("planner:home")


# UPDATE
# def Proyecto_update(request, pk: int):
#     query = models.Proyecto.objects.get(id=pk)
#     if request.method == "POST":
#         form = forms.ProyectoForm(request.POST, instance=query)
#         if form.is_valid:
#             form.save()
#             return redirect("Tarea:Proyecto_list")
#     else:  # request.method == "GET"
#         form = forms.ProyectoForm(instance=query)
#     return render(request, "Tarea/Proyecto_update.html", context={"form": form})


class ProyectoUpdate(UpdateView):
    model = models.Proyecto
    form_class = forms.ProyectoForm
    success_url = reverse_lazy("planner:proyecto_list")


# DETAIL
# def Proyecto_detail(request, pk: int):
#     query = models.Proyecto.objects.get(id=pk)
#     return render(request, "Tarea/Proyecto_detail.html", {"Tarea": query})


class ProyectoDetail(DetailView):
    model = models.Proyecto
    # context_object_name = "Tarea"


# DELETE
# def Proyecto_delete(request, pk: int):
#     query = models.Proyecto.objects.get(id=pk)
#     if request.method == "POST":
#         query.delete()
#         return redirect("Tarea:Proyecto_list")
#     return render(request, "Tarea/Proyecto_delete.html", context={"Tarea": query})


class ProyectoDelete(LoginRequiredMixin, DeleteView):
    model = models.Proyecto
    # template_name = "Tarea/Proyecto_delete.html"
    success_url = reverse_lazy("planner:proyecto_list")


# *** Tarea


class TareaList(ListView):
    model = models.Tarea

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Tarea.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Tarea.objects.all()
        return object_list


class TareaCreate(CreateView):
    model = models.Tarea
    form_class = forms.TareaForm
    success_url = reverse_lazy("planner:home")


class TareaUpdate(UpdateView):
    model = models.Tarea
    form_class = forms.TareaForm
    success_url = reverse_lazy("planner:tarea_list")


class TareaDetail(DetailView):
    model = models.Tarea


class TareaDelete(LoginRequiredMixin, DeleteView):
    model = models.Tarea
    success_url = reverse_lazy("planner:tarea_list")