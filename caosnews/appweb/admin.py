from django.contrib import admin
from .models import *




class PeriodistaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut', 'telefono', 'correo']

    
admin.site.register(Seccion)
admin.site.register(Periodista, PeriodistaAdmin)
admin.site.register(Noticia)
admin.site.register(Contacto)
admin.site.register(Curriculum)
# Register your models here.
