from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

def home (request):
    noticias = Noticia.objects.all()
    
    data = {
        'noticia' : noticias
    }
    
    return render(request, "home.html", data)
    
def contacto(request):
    
    data = {
        'form' : ContactoForm,
        'mensaje' : ""
    }
    
    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)    
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tu información ha sido enviada con exito")
        else:
            data['form'] = formulario
            messages.info(request, "Hubo un error")
    
    return render(request, "contacto.html", data)

@login_required(login_url="/accounts/login/")
@permission_required(['appweb.view_periodista'], login_url="/accounts/login/")
def listar_periodista(request):
    
    periodistas = Periodista.objects.all()
    
    data = {
        'periodistas' : periodistas
    }
    
    return render(request, "mantenedor/periodista/listar.html", data)

@login_required(login_url="/accounts/login/")
@permission_required(['appweb.change_noticia'], login_url="/accounts/login/")
def validar_noticia(request):
    
    noticia = Noticia.objects.all()
    
    data = {
        'noticia' : noticia
    }
    
    return render(request, "validacion_noticia.html", data)

@login_required(login_url="/accounts/login/")
@permission_required(['appweb.change_noticia'], login_url="/accounts/login/")
def aprobacion_noticia(request, id):

    noticia = get_object_or_404(Noticia, id=id)
    noticia.estado = 1
    noticia.save()  
    messages.success(request, 'La publicación ha sido aprobada')

    return redirect('validar_noticia')

def detalle_noticia(request, id):

    noticia = get_object_or_404(Noticia, id=id) 
    
    data = {
        "noticia": noticia
    }
    return render(request, "mantenedor/noticias/noticia_detalle.html", data)

@login_required(login_url="/accounts/login/")
@permission_required(['appweb.change_noticia'], login_url="/accounts/login/")
def rechazar_noticia(request, publicacion_id):
    if request.method == 'POST':
        motivo_rechazo = request.POST.get('motivo_rechazo')
        publicacion = Noticia.objects.get(id=publicacion_id)
        publicacion.estado = 2  # 2 representa el estado de "rechazado"
        publicacion.mensaje_rechazo = motivo_rechazo
        publicacion.save()
        messages.success(request, 'La publicación ha sido rechazada exitosamente.')
        return redirect('validar_noticia')
    else:
        messages.error(request, 'Se produjo un error al rechazar la publicación.')
        return redirect('validar_noticia')


def listar_seccion(request):
    
    secciones = Seccion.objects.all()
    
    data = {
        'secciones' : secciones
    }
    
    return render(request, "base.html", data)

def listar_noticias(request):
    
    noticias = Noticia.objects.all()
    
    data = {
        'noticia' : noticias
    }
        
    if request.method == "POST":
        valor_buscado = request.POST.get("valor_buscado")
        
        noticias = get_object_or_404(Noticia, periodista=valor_buscado)
        # noticias = Noticia.objects.get(periodista = valor_buscado)
        data["noticia"] = noticias
        
        
  
    return render(request, "mantenedor/noticias/noticia.html", data)

@login_required(login_url="/accounts/login/")
@permission_required(['appweb.change_periodista'], login_url="/accounts/login/")
def modificar_periodista(request, rut):
    
    periodista = get_object_or_404(Periodista, rut=rut)
    
    data = {
        "form": PeriodistaForm(instance=periodista)
    }
    
    if request.method == "POST":
        formulario = PeriodistaForm(data=request.POST, instance=periodista)
    
        if formulario.is_valid():
            messages.success(request, "Periodista modificado correctamente")
            formulario.save()
            return redirect(to="listar_periodista")

        else:
            data["form"] = formulario
            data["mensaje"] = "Ocurrio un error"
    
    return render(request, "mantenedor/periodista/modificar.html", data)

@login_required(login_url="/accounts/login/")
@permission_required(['appweb.delete_periodista'], login_url="/accounts/login/")
def eliminar_periodista(request, rut):
    
    periodista = get_object_or_404(Periodista, rut=rut)
    
    periodista.delete()
    
    return redirect(to=listar_periodista)

@login_required(login_url="/accounts/login/")
def login_usuario(request):
    messages.success(request, "Bienvenido")
    return redirect(to='home')

@login_required(login_url="/accounts/login/")
@permission_required(['appweb.add_periodista'], login_url="/accounts/login/")
def registro_usuario_periodista(request):
       
    data = {
        "mensaje": ""
    }
    
    if request.POST:
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        rut = request.POST.get("rut")
        telefono = request.POST.get("telefono")
        profesion = request.POST.get("profesion")
        
        if password1 != password2:
            data["mensaje"]= "Las contraseñas deben ser identicas"
            
        else:
           
            
            try:
                
                usu=User()
                usu.set_password(password1)
                usu.email=correo
                usu.username= nombre
                usu.last_name= apellido
                usu.first_name= nombre
                grupo = Group.objects.get(name='periodista')
                usu.save()
                  
                per = Periodista()
                per.rut = rut
                per.nombre = nombre
                per.apellido = apellido
                per.telefono = telefono
                per.profesion = profesion
                per.correo = correo
                per.usuario = usu
              
                per.save()
                usu.groups.add(grupo)
                messages.success(request, "Usuario/Periodista agregado correctamente")
                
                return redirect(to='home')
            except:
                data["mensaje"]="Error al grabar"
        
        
    return render(request, "registration/registro.html", data)

@login_required(login_url="/accounts/login/")
def vista_periodista(request):
    return render(request, "periodista.html")

@login_required(login_url="/accounts/login/")
def agregar_noticia(request):
    
    data = {
        
        'form': NoticiaForm
    }
    
    if request.method == "POST":
        form = NoticiaForm(data=request.POST, files=request.FILES)
        
        if form.is_valid():
            titulo = form.cleaned_data.get('titulo')
            informacion = form.cleaned_data.get('informacion')
          #  periodista = form.cleaned_data.get('periodista')
            seccion = form.cleaned_data.get('seccion')
            foto = form.cleaned_data.get('foto')
            fecha = form.cleaned_data.get('fecha_noticia')
            ubicacion = form.cleaned_data.get('ubicacion')

            noticia = Noticia()
            noticia.titulo = titulo
            noticia.informacion = informacion
            noticia.seccion = seccion
            noticia.foto = foto
            noticia.fecha_noticia = fecha
            noticia.ubicacion = ubicacion
            usu = request.user
            
            periodista = Periodista.objects.get(usuario = usu)
            
            
            noticia.periodista = periodista
            noticia.save()
            messages.success(request, 'Publicación a la espera de revisión')
            return redirect('vista_periodista')
        
        else: 
            form = NoticiaForm()

    
    return render(request, "mantenedor/noticias/agregar.html", data)

@login_required(login_url="/accounts/login/")
@permission_required(['appweb.view_periodista'], login_url="/accounts/login/")
def vista_administrador(request):
    
     return render(request, "admin.html")

@login_required(login_url="/accounts/login/")
def estado_noticia(request):

    noticia = Noticia.objects.all()
    
    data = {
        "noticia": noticia
    }

    return render(request, "estado_noticia.html", data)

def curriculum(request):
    data = {
        'form' : CurriculumForm,
        'mensaje' : ""
    }
    
    if request.method == "POST":
        formulario = CurriculumForm(request.POST, request.FILES)    
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tu información ha sido enviada con exito")
            return redirect('home')
        else:
            data['form'] = formulario
            messages.warning(request, "Hubo un error")
    
    return render(request, "curriculum.html", data)

@login_required(login_url="/accounts/login/")
@permission_required(['appweb.view_curriculum'], login_url="/accounts/login/")
def listar_curriculum(request):
    
    curriculums = Curriculum.objects.all()
    
    data = {
        'curriculums' : curriculums
    }
    
    return render(request, "listar_curriculum.html", data)

@login_required(login_url="/accounts/login/")
@permission_required(['appweb.view_curriculum'], login_url="/accounts/login/")
def detalle_curriculum (request, id):

    curriculum = get_object_or_404(Curriculum, id=id) 
    
    data = {
        "curriculum": curriculum
    }
    return render(request, "detalle_curriculum.html", data)

def listar_categoria(request, seccion):
    
    noticias =  Noticia.objects.filter(seccion = seccion)
    
    data = {
        'noticia' : noticias
    }
    
    return render(request, "listar_categoria.html", data)