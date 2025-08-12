from django.conf import settings
from django.contrib import admin
from django.urls import path
from contenido import views
from django.conf import settings 
from cursos import views as views_cursos
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name="Principal"),
    path('cursos/', views_cursos.cursos, name='Cursos'),
    path('contacto/',views.contacto, name="Contacto"),
    path('registrar/', views_cursos.registrar, name='Registrar'),
    path('ver_cursos/', views_cursos.verCursos, name='ver_cursos'),
    path('editar_curso/<int:id>/', views_cursos.editarCurso, name='editar_curso'),
    path('eliminarCurso/<int:id>/',views_cursos.eliminarCurso ,name='Eliminar'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)