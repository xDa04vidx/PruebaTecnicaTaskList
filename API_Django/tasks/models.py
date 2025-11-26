from django.db import models

class Tasks(models.Model):
    title               = models.CharField(max_length=255, null=False,verbose_name="titulo")
    description         = models.CharField(max_length=255, null=False,verbose_name="descripcion")
    create_date_task    = models.DateField(null=False, verbose_name="fecha_creacion")
    finish_planned_date = models.DateField(null=False, verbose_name="fecha_fin_planeada")
    real_finish_date    = models.DateField(null=False, verbose_name="fecha_fin_real")
    