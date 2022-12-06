from rest_framework import serializers
from profiles_app import models

class HelloSerializer(serializers.Serializer):
  """ Serializa un campo para probar la APIView"""
  name = serializers.CharField(max_length=10)
  
class UserProfileSerializer(serializers.ModelSerializer):
  """ Serializa objeto de perfil de usuario """

  class Meta:
    model = models.UserProfile
    fields = ("id", "email", "name", "password")
    extra_kwargs = {
      "password": {
        "write_only": True,
        "style": {"input_type": "password"}
      }
    }


  def create(self, validated_data):
    """ Crear y retornar un nuevo usuario """

    user = models.UserProfile.objects.create_user(
      email = validated_data["email"],
      name = validated_data["name"],
      password = validated_data["password"]
    )

    return user


  def update(self,instance, validate_data):
    """ Actualiza una cuenta de usuario  """

    if "password" in validate_data:
      password = validate_data.pop("password")
      instance.set_password(password)

    return super().update(instance, validate_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
  """ SErializador de profile feed items """

  class Meta:
    model = models.ProfileFeedItem
    fields = ("id", "user_profile", "status_text", "created_on")
    extra_kwargs = {"user_profile": {"read_only": True}}