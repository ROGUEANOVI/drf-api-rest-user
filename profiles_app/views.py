# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_app import serializers, models, permissions
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class HelloApiView(APIView):
  """ Api View de prueba"""

  serializer_class = serializers.HelloSerializer

  def get(self, request, format=None):
    """ Retornar lista de caracteriaticas del APIView"""

    an_apiview = [
      "Usamos metodos HTTP como funciones (get, post, pach, put, delete)",
      "Es similar a una vista tradicional de Django",
      "Nos da mayor control sobre la logica de nuestra aplicacion",
      "Esta mapeada manualmente a los URLs",
    ]

    return Response({"message": "Hello", "an_apiview": an_apiview})


  def post(self, request):
    """ Crea un mensaje con nuestro nombre """

    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get("name")
      message = f"Hello {name}"
      return Response({"message":message})
    
    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
      )

  
  def put(self, request, pk=None):
    """ Actualiza un objeto """
    return Response({"method": "PUT"})
 
 
  def patch(self, request, pk=None):
    """ Actualiza parcialmente un objeto """
    return Response({"method": "PATCH"})

  def delete(self, request, pk=None):
    """ Elimina un objeto """
    return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
  """ View set de prueba """

  serializer_class = serializers.HelloSerializer

  def list(self, request):
    """ Retornar mensaje Hello World"""
    
    a_viewset = [
      "Usamos acciones (list, create, reatrive, update, partial_update, destroy)",
      "Nos da mayor funcuionalidad de nuestra aplicacion con menos codigo",
      "Mapea automaticamente a los URLs usando Routers",
    ]

    return Response({ "message": "Hello World" , "a_viewset": a_viewset})

  def create(self, request):
    """ Crear nuevo mensaje Hola Mundo"""
    
    serializer = self.serializer_class(data=request.data)
    
    if serializer.is_valid():
      name = serializer._validated_data.get("name")
      message = f"Hola {name}"
      return Response({"message":message})

    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
      )

  def retrieve(self, request, pk=None):
    """ Obtiene un objeto y su ID"""

    return Response({"http_method": "GET"})
  

  def update(self, request, pk=None):
    """ Actualiza un objeto """

    return Response({"http_method": "PUT"})

  
  def partial_update(self, request, pk=None):
    """ Actualiza parcialmente un objeto """

    return Response({"http_method": "PATCH"})

  def destroy(self, request, pk=None):
    """ Elimina un objeto"""

    return Response({"http_method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
  """ View set de un perfil de usuario """

  serializer_class = serializers.UserProfileSerializer
  queryset = models.UserProfile.objects.all()
  authentication_classes = (TokenAuthentication, )
  permission_classes = (permissions.UpdateOwnProfile, )
  filter_backends = (filters.SearchFilter, )
  search_fields = ("name", "email")


class UserLoginApiView(ObtainAuthToken):
  """ Crea tokens de autenticacion de usuarios """
  renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
  """ View set para crear, leer y actualizar el profile feed  """

  serializer_class = serializers.ProfileFeedItemSerializer
  queryset = models.ProfileFeedItem.objects.all()
  authentication_classes = (TokenAuthentication, )
  permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

  def perform_create(self, serializer):
    """ Setear el perfil de usuario para el el usuario logueado """

    serializer.save(user_profile=self.request.user)
