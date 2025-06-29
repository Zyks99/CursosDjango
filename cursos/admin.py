from django.contrib import admin
from .models import Cursos
# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
     readonly_fields=('created','updated')    
     list_display=('created','nombre','estatus','image','precio','duracion','fecha_inicio','updated')  
     search_fields=('nombre','fecha_inicio','estatus')
     date_hierarchy='created'
     list_filter=('nombre','estatus','created')  
admin.site.register(Cursos,AdministrarModelo)