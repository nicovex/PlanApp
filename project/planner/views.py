# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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

@login_required
def home(request):
    # return render(request, "planner/index.html")

    # proyectos = models.Proyecto.objects.all()
    # proyectos_data = []

    # for proyecto in proyectos:
    #     total_tareas = proyecto.tareas.count()
    #     tareas_completadas = proyecto.tareas.filter(completada=True).count()
    #     tareas_no_completadas = total_tareas - tareas_completadas
    #     proyectos_data.append({
    #         'nombre': proyecto.nombre,
    #         'total_tareas': total_tareas,
    #         'tareas_completadas': tareas_completadas,
    #         'tareas_no_completadas': tareas_no_completadas,
    #     })

    # context = {
    #     'proyectos_data': proyectos_data,
    # }
    return render(request, 'planner/index.html') #context)


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


class ProyectoList(ListView, LoginRequiredMixin):
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


class ProyectoCreate(CreateView, LoginRequiredMixin):
    model = models.Proyecto
    form_class = forms.ProyectoForm
    success_url = reverse_lazy("planner:home")

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     if self.request.POST:
    #         data['formset'] = forms.TareaFormSet(self.request.POST)
    #     else:
    #         data['formset'] = forms.TareaFormSet(queryset=models.Tarea.objects.none())
    #     return data

    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     formset = context['formset']
    #     if formset.is_valid():
    #         self.object = form.save(commit=False)  # Guardar el proyecto sin confirmarlo aún
    #         tareas = formset.save(commit=False)  # Guardar las tareas sin confirmarlas aún
    #         self.object.save()  # Ahora guardar el proyecto para obtener el ID
    #         for tarea in tareas:
    #             tarea.proyecto = self.object  # Asignar el proyecto a cada tarea
    #             tarea.save()  # Guardar la tarea con la relación al proyecto
    #         return redirect(self.get_success_url())
    #     else:
    #         return self.form_invalid(form)


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


class ProyectoUpdate(UpdateView, LoginRequiredMixin):
    model = models.Proyecto
    form_class = forms.ProyectoForm
    success_url = reverse_lazy("planner:proyecto_list")

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     if self.request.POST:
    #         data['formset'] = forms.TareaFormSet(self.request.POST, instance=self.object)
    #     else:
    #         data['formset'] = forms.TareaFormSet(queryset=models.Tarea.objects.filter(proyecto=self.object))
    #     return data

    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     formset = context['formset']
    #     if formset.is_valid():
    #         self.object = form.save(commit=False)  # Guardar el proyecto sin confirmarlo aún
    #         tareas = formset.save(commit=False)  # Guardar las tareas sin confirmarlas aún
    #         self.object.save()  # Ahora guardar el proyecto para obtener el ID
    #         for tarea in tareas:
    #             tarea.proyecto = self.object  # Asignar el proyecto a cada tarea
    #             tarea.save()  # Guardar la tarea con la relación al proyecto
    #         return redirect(self.get_success_url())
    #     else:
    #         return self.form_invalid(form)


# DETAIL
# def Proyecto_detail(request, pk: int):
#     query = models.Proyecto.objects.get(id=pk)
#     return render(request, "Tarea/Proyecto_detail.html", {"Tarea": query})


class ProyectoDetail(DetailView, LoginRequiredMixin):
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


class TareaList(ListView, LoginRequiredMixin):
    model = models.Tarea

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Tarea.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Tarea.objects.all()
        return object_list


class TareaCreate(CreateView, LoginRequiredMixin):
    model = models.Tarea
    form_class = forms.TareaForm
    # proyecto = models.Tarea.proyecto
    success_url = reverse_lazy("planner:home")


class TareaUpdate(UpdateView, LoginRequiredMixin):
    model = models.Tarea
    form_class = forms.TareaForm
    success_url = reverse_lazy("planner:tarea_list")


class TareaDetail(DetailView, LoginRequiredMixin):
    model = models.Tarea


class TareaDelete(LoginRequiredMixin, DeleteView):
    model = models.Tarea
    success_url = reverse_lazy("planner:tarea_list")

class ResponsableUpdate(LoginRequiredMixin, UpdateView):
    model = models.Responsable
    form_class = forms.ResponsableForm
    success_url = reverse_lazy("planner:responsable_list")

class ResponsableList(ListView, LoginRequiredMixin):
    model = models.Responsable

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Responsable.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Responsable.objects.all()
        return object_list