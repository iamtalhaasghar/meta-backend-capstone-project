from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import *

router = DefaultRouter()
router.register('users', UserViewSet) 

urlpatterns = [
    path('', include(router.urls)), 
    path("menu/", MenuItemView.as_view(), name=""),
    path("menu/<int:pk>", SingleMenuItemView.as_view(), name=""),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) 
]
