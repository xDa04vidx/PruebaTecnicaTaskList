from django.db import models

class Tasks(models.Model):
    title               = models.CharField(max_length=255, null=False, verbose_name="titulo")
    description         = models.TextField(null=False, verbose_name="descripcion")  # Debería ser TextField si es más largo
    create_date_task    = models.DateTimeField(null=False, verbose_name="fecha_creacion")  # Debería ser DateTimeField
    finish_planned_date = models.DateTimeField(null=False, verbose_name="fecha_fin_planeada")  # Debería ser DateTimeField
    real_finish_date    = models.DateTimeField(null=True, blank=True, verbose_name="fecha_fin_real")  # Debería ser DateTimeField y puede ser nulo
    create_date         = models.DateTimeField(auto_now_add=True, verbose_name="fecha_creacion")  # Automatically set to current timestamp
    modificated_date    = models.DateTimeField(auto_now=True, verbose_name="fecha_modificacion")  # Automatically set to current timestamp
    create_user         = models.CharField(max_length=50, null=False, verbose_name="usuario_creacion", default='current_user')  # Adjust default as needed
    modificate_user     = models.CharField(max_length=50, null=False, verbose_name="usuario_modificacion", default='current_user')  # Adjust default as needed

    class Meta:
        db_table = 'task' 
