from django.conf.urls import url
from django.urls import path
from portafolio.views import index, pollas, pollos, animales_en_proceso, animales_en_inicio_de_proceso, crestones

app_name = 'portafolio'
urlpatterns = [
    path('', index.as_view(), name='index'),
    url(r'^pollas', pollas.as_view(), name='categoria_pollas'),
    url(r'^pollos', pollos.as_view(), name='categoria_pollos'),
    url(r'^animales_en_proceso', animales_en_proceso.as_view(), name='animales_en_proceso'),
    url(r'^animales_en_inicio_de_proceso', animales_en_inicio_de_proceso.as_view(), name='animales_en_inicio_de_proceso'),
    url(r'^crestones', crestones.as_view(), name='categoria_crestones'),
]
