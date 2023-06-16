from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from .user_models import User


class Clase1(models.Model):
    campo1 = models.CharField(max_length=100)
    # Agrega otros campos según tus necesidades

class Clase2(models.Model):
    campo1 = models.CharField(max_length=100)
    # Agrega otros campos según tus necesidades

class Clase3(models.Model):
    campo1 = models.CharField(max_length=100)
    # Agrega otros campos según tus necesidades



