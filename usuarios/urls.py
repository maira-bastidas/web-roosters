from django.urls import path

from usuarios.views import RegistrarUsuario

app_name = 'usuarios'
urlpatterns = [
    path('registrar_usuario', RegistrarUsuario.as_view(), name='registrar_usuario')
]