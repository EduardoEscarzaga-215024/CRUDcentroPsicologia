
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('Usuarios.urls')),
    path('', include('Inicio.urls')),
    path('citas/', include('Citas.urls')),
]
