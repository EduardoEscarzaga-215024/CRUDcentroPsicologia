from django.urls import path
from . import views

urlpatterns = [
    path('agendar/', views.agendar_cita, name='agendar_cita'),
    path('lista/', views.lista_citas, name='lista_citas'),
    path('editar/<int:cita_id>/', views.editar_cita, name='editar_cita'),
    path('eliminar/<int:cita_id>/', views.eliminar_cita, name='eliminar_cita'),
]