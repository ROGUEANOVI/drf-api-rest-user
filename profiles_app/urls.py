from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet, UserProfileViewSet, UserLoginApiView, UserProfileFeedViewSet

router = DefaultRouter()
router.register("hello-viewset", HelloViewSet, basename="hello_viewset")
router.register("profile", UserProfileViewSet, basename="profile")
router.register("feed", UserProfileFeedViewSet, basename="feed")
 
urlpatterns = [
  path('hello-apiview/', HelloApiView.as_view(), name='hello_apiview'),
  path('login/', UserLoginApiView.as_view(), name='login'),
  path('', include(router.urls)),
]

