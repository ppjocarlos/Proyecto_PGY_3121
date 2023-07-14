from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Seccion(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Periodista(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    telefono = models.IntegerField()
    profesion = models.CharField(max_length=80)
    correo = models.EmailField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.rut

estados = [
    [0, "En Espera"],
    [1, "Aprobado"],
    [2, "Rechazado"]
]

class Noticia (models.Model):
    titulo = models.CharField(max_length= 500)
    informacion = models.TextField(null=True)
    foto = models.ImageField( null=True, upload_to ='noticias')
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    periodista = models.ForeignKey(Periodista, on_delete=models.CASCADE)
    estado = models.IntegerField(choices=estados, default=0)
    ubicacion = models.CharField(null=True, max_length=100)
    fecha_noticia = models.DateField(null=True)
    mensaje_rechazo = models.TextField(max_length=200, null=True)
     
    def __str__(self):
        return self.titulo

list_tipo_contacto = [
    [0,"Sugerencia"],
    [1,"Reclamo"],
    [2,"Felicitaciones"]
]
class Contacto (models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    tipo_contacto = models.IntegerField(choices = list_tipo_contacto)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre

class Curriculum (models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    telefono = models.IntegerField()
    correo = models.EmailField()
    ubicacion = models.CharField(max_length= 100)
    profesion = models.CharField(max_length= 50)
    experiencia = models.TextField(null=True)
    educacion = models.TextField(null=True)
    foto = models.ImageField( null=True, upload_to ='curriculums')
    
    def __str__(self):
        
        return self.nombre