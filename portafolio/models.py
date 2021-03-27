from django.db import models

# Create your models here.
class Categoria (models.Model):
    nombre_categoria = models.CharField(max_length=300, null=True, blank=False, verbose_name='Nombre_categoria')
    descripcion = models.TextField(null=True, blank=False,help_text='ingrese una descripcipón del animal', verbose_name='Descripcion animal')

    def __str__(self):
        return self.nombre_categoria

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering =['-id']

class Producto(models.Model):
    nombre_gallo = models.CharField(max_length=200, null=True, blank=False, verbose_name='Nombre_gallo')
    slug = models.SlugField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField(null=True, blank=False, help_text='ingrese una descripcipón del animal',
                                   verbose_name='Descripcion animal')
    precio = models.IntegerField(null=True, blank=False)
    origen_animal = models.TextField(null=True, blank=False, help_text='ingrese el origen del animal',
                                     verbose_name='origen_animal')
    foto = models.ImageField(upload_to='portafolio/static/images', verbose_name='Foto_animal', null=True, blank=True)

    disponible = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
