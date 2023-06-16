from django.shortcuts import render, redirect
from django.views import View
from .forms import Clase1Form, Clase2Form, Clase3Form, UsuarioForm
from .models import Clase1, Clase2, Clase3
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BaseView(View):
    def get(self, request):
        # Lógica para el método GET
        return render(request, 'base.html')

    def post(self, request):
        # Lógica para el método POST
        return render(request, 'base.html')

class Clase1View(View):
    def get(self, request):
        form = Clase1Form()
        usuario_form = UsuarioForm()
        return render(request, 'base.html', {'form': form, 'usuario_form': usuario_form})

    def post(self, request):
        form = Clase1Form(request.POST)
        if form.is_valid():
            # Guardar el formulario de usuario
            user_form = UserCreationForm(request.POST)
            if user_form.is_valid():
                user = user_form.save()
                # Aquí puedes realizar otras acciones con el objeto de usuario si es necesario

            # Guardar el formulario de Clase1Form
            form.save()
            return redirect('Inicio')
        return render(request, 'base.html', {'form': form})

class Clase2View(View):
    def get(self, request):
        objetos = Clase2.objects.all()
        form = Clase2Form()
        return render(request, 'clase2.html', {'form': form, 'objetos': objetos})

    def post(self, request):
        form = Clase2Form(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            try:
                Clase2.objects.get(usuario=usuario)
                usuario_encontrado = True
            except Clase2.DoesNotExist:
                usuario_encontrado = False

            return render(request, 'clase2.html', {'form': form, 'usuario_encontrado': usuario_encontrado})

        return render(request, 'clase2.html', {'form': form})

class Clase3View(View):
    def get(self, request):
        objetos = Clase3.objects.all()
        form = Clase3Form()
        return render(request, 'clase3.html', {'form': form, 'objetos': objetos})

    def post(self, request):
        form = Clase3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Registro')
        return render(request, 'base.html', {'form': form})

class UsuarioView(View):
    def get(self, request):
        form = UsuarioForm()
        return render(request, 'base.html', {'form': form})

    def post(self, request):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            contraseña = form.cleaned_data['contraseña']
            return redirect('clase1')
        return render(request, 'base.html', {'form': form})