from django.db import models
from ckeditor.fields import RichTextField
from django.shortcuts import render, redirect
class Cursos(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")

    nombre = models.CharField(max_length=100, verbose_name="Nombre del Curso") 

    descripcion = RichTextField(verbose_name="Descripción del Curso", default="Descripción detallada del curso.")

    image = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")

    estatus = models.BooleanField(default=True, verbose_name="Activo") 

    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio del Curso")

    duracion = models.IntegerField(default=0, verbose_name="Duración (horas)")

    fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha de Inicio") # Added blank=True

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")


    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre 
class Actividades(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave Actividad")
    curso = models.ForeignKey(Cursos,
    on_delete=models.CASCADE,verbose_name="Curso")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    updated=models.DateTimeField(auto_now_add=True,verbose_name="Actualización")
    description = RichTextField(verbose_name="Descripción Actividad")
    class Meta:
        verbose_name ="Actividad"
        verbose_name_plural ="Actividades"
        ordering = ["created"]
    def __str__(self):
        return self.description