from django.db import models

# Create your models here.
class Cursos(models.Model): 
    nombre=models.TextField(max_length=20)
    image=models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografia")
    estatus = models.BooleanField(default=True,verbose_name="Estatus")
    precio = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Precio")
    duracion= models.IntegerField(default=0,verbose_name="Duración en horas")
    fecha_inicio = models.DateField(null=True,verbose_name="Fecha de inicio")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de actualización")

    class Meta:
        verbose_name ="Curso"
        verbose_name_plural ="Cursos"
        ordering = ["created"]# el menos determina si es ascendente o descendente
    def __str__(self):
        return self.nombre     