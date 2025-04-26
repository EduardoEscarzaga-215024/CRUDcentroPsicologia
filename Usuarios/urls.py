from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registrar_recepcionista, name='registro_recepcionista'),
    path('login/', views.login_recepcionista, name='login'),
    path('logout/', views.logout_recepcionista, name='logout'),
]