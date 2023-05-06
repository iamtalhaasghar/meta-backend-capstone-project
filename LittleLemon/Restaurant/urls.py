from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import *
#import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
# router.register('users', UserViewSet) 
router.register('tables', BookingViewSet)

urlpatterns = [
    path('booking/', include(router.urls)), 
    path("menu/", MenuItemView.as_view(), name=""),
    path("menu/<int:pk>", SingleMenuItemView.as_view(), name=""),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) ,
    path("message/", msg, name=""),
    path('api-token-auth/', obtain_auth_token),
]
