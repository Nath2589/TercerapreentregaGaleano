from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    # Agrega campos adicionales si es necesario

    class Meta(AbstractUser.Meta):
        # Agrega el atributo unique_together para evitar conflictos con las claves únicas
        swappable = 'AUTH_USER_MODEL'
        unique_together = ('username',)

    groups = models.ManyToManyField('auth.Group', verbose_name=_('groups'), blank=True, help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'), related_name='user_set', related_query_name='user')
    user_permissions = models.ManyToManyField('auth.Permission', verbose_name=_('user permissions'), blank=True, help_text=_('Specific permissions for this user.'), related_name='user_set', related_query_name='user')

    # Aquí puedes agregar métodos o atributos adicionales según tus necesidades

    def __str__(self):
        return self.username
