"""
URL configuration for PreentregaWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import Clase1View, Clase2View, Clase3View

urlpatterns = [
    path('clase1/', Clase1View.as_view(), name='Inicio'),
    path('clase2/', Clase2View.as_view(), name='Detalles'),
    path('clase3/', Clase3View.as_view(), name='Registro'),
]

