from django import forms
from .models import Clase1, Clase2, Clase3
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Clase1Form(forms.ModelForm):
    class Meta:
        model = Clase1
        fields = '__all__'

class Clase2Form(forms.ModelForm):
    class Meta:
        model = Clase2
        fields = '__all__'

class Clase3Form(forms.ModelForm):
    class Meta:
        model = Clase3
        fields = '__all__'

class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': _('Nombre de usuario'),
            'password1': _('Contraseña'),
            'password2': _('Confirmar contraseña'),
        }
        help_texts = {
            'username': _('Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.'),
            'password1': _('Tu contraseña no puede ser demasiado similar a tu otra información personal. Debe contener al menos 8 caracteres. No puede ser una contraseña común. No puede ser completamente numérica.'),
        }
        error_messages = {
            'password2': {
                'password_mismatch': _('Las contraseñas no coinciden.'),
            },
        }