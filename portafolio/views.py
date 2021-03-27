from django.shortcuts import render
from django.views import View
from  portafolio.models import Producto, Categoria
# Create your views here.

class index(View):
    template_name = 'portafolio/index.html'

    def get(self, request, *args, **kwargs):
        productos = Producto.objects.all()
        return render(request, self.template_name, {'productos':productos})

class pollas(View):
    model = Producto
    template_name = 'portafolio/categoria_pollas.html'

    def get(self, request, *args, **kwargs):
        categoria = Categoria.objects.get(nombre_categoria='Pollas')
        pollas = Producto.objects.filter(categoria=categoria, disponible=True)
        return render(request, self.template_name, {'pollas':pollas})

class pollos(View):
    model = Producto
    template_name = 'portafolio/categoria_pollos.html'

    def get(self, request, *args, **kwargs):
        categoria = Categoria.objects.get(nombre_categoria='Pollos')
        pollos = Producto.objects.filter(categoria=categoria, disponible=True)
        return render(request, self.template_name, {'pollos':pollos})

class animales_en_proceso(View):
    model = Producto
    template_name = 'portafolio/categoria_animales_en_proceso.html'

    def get(self, request, *args, **kwargs):
        categoria = Categoria.objects.get(nombre_categoria='Animales en proceso de cuido')
        animales_en_proceso = Producto.objects.filter(categoria=categoria, disponible=True)
        return render(request, self.template_name, {'animales_en_proceso':animales_en_proceso})

class crestones(View):
    model = Producto
    template_name = 'portafolio/crestones.html'

    def get(self, request, *args, **kwargs):
        categoria = Categoria.objects.get(nombre_categoria='Crestones')
        crestones = Producto.objects.filter(categoria=categoria, disponible=True)
        return render(request, self.template_name, {'crestones':crestones})


class animales_en_inicio_de_proceso(View):
    model = Producto
    template_name = 'portafolio/categoria_pollos_en_inicio_de_proceso.html'

    def get(self, request, *args, **kwargs):
        categoria = Categoria.objects.get(nombre_categoria='Pollos en proceso de inicio de cuido')
        animales_en_inicio_de_proceso = Producto.objects.filter(categoria=categoria, disponible=True)
        return render(request, self.template_name, {'animales_en_inicio_de_proceso':animales_en_inicio_de_proceso})
