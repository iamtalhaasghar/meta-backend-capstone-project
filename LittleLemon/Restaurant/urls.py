from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import hello, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet) 

urlpatterns = [
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) 
]
