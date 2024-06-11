from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from clientes.views import ClientesViewSet

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include(router.urls)),
]
