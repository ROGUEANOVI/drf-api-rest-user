from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
  """ Permite a ususarios editar solo su propio usuario"""

  def has_object_permission(self, request, view, obj):
    """ Revisar si el usuario esta intentando editar su propio perfil """
    
    if request.method in permissions.SAFE_METHODS:
      return True
    
    return obj.id == request.user.id
  

class UpdateOwnStatus(permissions.BasePermission):
  """ Permite actualizar el propio status feed """

  def has_object_permission(self, request, view, obj):
    """ Revisar si el usuario esta intentando editar su propio perfil """

    if request.method in permissions.SAFE_METHODS:
      return True

    return obj.user_profile_id == request.user.id
