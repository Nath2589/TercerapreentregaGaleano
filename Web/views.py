from django.shortcuts import render, redirect
from django.views import View
from .forms import Clase1Form, Clase2Form, Clase3Form
from .models import Clase1, Clase2, Clase3

class Clase1View(View):
    def get(self, request):
        # Aquí puedes realizar operaciones relacionadas con Clase1
        # por ejemplo, obtener objetos de la base de datos
        objetos = Clase1.objects.all()

        form = Clase1Form()
        return render(request, 'clase1.html', {'form': form, 'objetos': objetos})

    def post(self, request):
        form = Clase1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_url')
        return render(request, 'clase1.html', {'form': form})

class Clase2View(View):
    def get(self, request):
        # Aquí puedes realizar operaciones relacionadas con Clase2
        # por ejemplo, obtener objetos de la base de datos
        objetos = Clase2.objects.all()

        form = Clase2Form()
        return render(request, 'clase2.html', {'form': form, 'objetos': objetos})

    def post(self, request):
        form = Clase2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Detalles')
        return render(request, 'clase2.html', {'form': form})

class Clase3View(View):
    def get(self, request):
        # Aquí puedes realizar operaciones relacionadas con Clase3
        # por ejemplo, obtener objetos de la base de datos
        objetos = Clase3.objects.all()

        form = Clase3Form()
        return render(request, 'clase3.html', {'form': form, 'objetos': objetos})

    def post(self, request):
        form = Clase3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Registro')
        return render(request, 'clase3.html', {'form': form})

