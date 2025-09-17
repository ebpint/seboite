from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ListaNegra, Operacion

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'perfil', 'is_staff', 'created_at']
    list_filter = ['perfil', 'is_staff', 'is_active', 'created_at']
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('perfil',)}),
    )

@admin.register(ListaNegra)
class ListaNegraAdmin(admin.ModelAdmin):
    list_display = ['archivo_nombre', 'cargado_por', 'fecha_carga', 'activo']
    list_filter = ['fecha_carga', 'activo', 'cargado_por']
    readonly_fields = ['fecha_carga']
    search_fields = ['archivo_nombre']

@admin.register(Operacion)
class OperacionAdmin(admin.ModelAdmin):
    list_display = ['archivo_nombre', 'cargado_por', 'fecha_carga', 'activo']
    list_filter = ['fecha_carga', 'activo', 'cargado_por']
    readonly_fields = ['fecha_carga']
    search_fields = ['archivo_nombre']