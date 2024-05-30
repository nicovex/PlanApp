# Generated by Django 5.0.6 on 2024-05-30 18:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_alter_tarea_proyecto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='tareas',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='responsable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proyectos_responsable', to=settings.AUTH_USER_MODEL),
        ),
    ]
