from django import forms
from .models import Contacto, Periodista, Noticia, User, Curriculum

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        
        fields = "__all__"

class PeriodistaForm(forms.ModelForm):
    
    class Meta:
        model = Periodista
        fields = "__all__"
class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields = ["titulo","foto", "seccion", "fecha_noticia", "ubicacion", "informacion"]
        
    widgets = {
        "fecha_noticia": forms.DateInput(attrs={'type':'date'}, format=('%Y-%m-%d'))
    }
    
class CurriculumForm(forms.ModelForm):
    
    class Meta:
        model = Curriculum
        fields = ["foto", "nombre", "apellido", "telefono", "correo", "ubicacion", "profesion", "educacion", "experiencia" ]