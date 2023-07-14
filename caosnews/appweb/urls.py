from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('listar_periodista/', listar_periodista, name="listar_periodista"),
    path('modificar_periodista/<rut>/', modificar_periodista, name="modificar_periodista"),
    path('eliminar_periodista/<rut>/', eliminar_periodista, name="eliminar_periodista"),
    path('login_usuario/', login_usuario, name="login_usuario"),
    path('registro_usuario/', registro_usuario_periodista, name="registro_usuario"),
    path('vista_periodista/', vista_periodista, name="vista_periodista"),
    path('agregar_noticia/', agregar_noticia, name="agregar_noticia"),
    path('vista_administrador/', vista_administrador, name="vista_administrador"),
    path('validar_noticia/', validar_noticia, name="validar_noticia"),
    path('estado_noticia/', estado_noticia, name="estado_noticia"),
    path('aprobacion_noticia/<int:id>/', views.aprobacion_noticia, name='aprobacion_noticia'),
    path('rechazar_noticia/<int:publicacion_id>/', views.rechazar_noticia, name='rechazar_noticia'),
    path('listar_noticias/', listar_noticias, name='listar_noticias'),
    path('noticia_detalle/<int:id>/', detalle_noticia, name='noticia_detalle'),
    path('curriculum/', curriculum, name="curriculum"),
    path('listar_curriculum/', listar_curriculum, name="listar_curriculum"),
    path('detalle_curriculum/<int:id>/', detalle_curriculum, name='detalle_curriculum'),
    path('listar_categoria/<seccion>/', listar_categoria, name='listar_categoria')    
]

