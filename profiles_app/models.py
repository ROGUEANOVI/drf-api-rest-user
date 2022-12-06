from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Create your models here.

class UserProfileManager(BaseUserManager):
  """ Manager para Perfiles de Usuario """

  def create_user(self, email, name, password=None):
    """ Crear nuevo User Profile """
    if not email:
      raise ValueError("El Usuario debe tener un email")
    
    email = self.normalize_email(email)

    user = self.model(email=email, name=name)
    user.set_password(password)
    user.save(using=self._db)

    return user


  def create_superuser(self, email, name, password):
    user = self.create_user(email, name, password)

    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)

    return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
  """ Modelo base de datos para Usuarios en el sistema """

  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserProfileManager()

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["name"]

  def get_full_name(self):
    """ Obtener nombre completo del Usuario """
    return self.name

  def get_short_name(self):
    """ Mostrar nombre corto del Usuario """
    return self.name
  
  def __str__(self):
    """ Retonrnar cadena representando el usuario """
    return self.email


class ProfileFeedItem(models.Model):
  """ Perfil de status update """

  user_profile = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE
  )
  status_text = models.CharField(max_length=255)
  created_on = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    """ Retornar el modelo como cadena de texto """

    return self.status_text