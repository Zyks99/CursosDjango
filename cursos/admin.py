from django.contrib import admin
from .models import Cursos
from .models import Actividades
# Register your models here.
class AdministrarCursos(admin.ModelAdmin):
     #readonly_fields=('created','updated')    
     list_display=('nombre','estatus','image','precio','duracion','fecha_inicio')  
     search_fields=('nombre','fecha_inicio','estatus')
     #date_hierarchy='created'
     list_filter=('nombre','estatus')  
admin.site.register(Cursos,AdministrarCursos)

class AdministrarActividades(admin.ModelAdmin):
     list_display=('id','curso','description','created')
     search_fields=('id','description')
     date_hierarchy='created'
     readonly_fields=('created','updated')
admin.site.register(Actividades,AdministrarActividades)