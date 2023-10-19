from django.urls import path
from galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'), #name é para usar nos templates {% url 'imagem' %}
    path('buscar', buscar, name="buscar")
]