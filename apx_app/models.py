from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    PERFIL_CHOICES = [
        ('oficial', 'Oficial de Cumplimiento'),
        ('analista', 'Analista'),
        ('sistemas', 'Sistemas'),
    ]

    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"{self.username} - {self.get_perfil_display()}"


class ListaNegra(models.Model):
    archivo_nombre = models.CharField(max_length=255)
    fecha_carga = models.DateTimeField(default=timezone.now)
    cargado_por = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='listas_negras/')
    contenido = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['-fecha_carga']
        verbose_name = 'Lista Negra'
        verbose_name_plural = 'Listas Negras'

    def __str__(self):
        return f"{self.archivo_nombre} - {self.fecha_carga}"


class Operacion(models.Model):
    archivo_nombre = models.CharField(max_length=255)
    fecha_carga = models.DateTimeField(default=timezone.now)
    cargado_por = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='operaciones/')
    contenido = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['-fecha_carga']
        verbose_name = 'Operación'
        verbose_name_plural = 'Operaciones'

    def __str__(self):
        return f"{self.archivo_nombre} - {self.fecha_carga}"