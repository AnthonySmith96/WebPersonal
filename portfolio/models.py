from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length = 100, verbose_name = 'Titulo')
    content = models.TextField(verbose_name = 'Contenido')
    image = models.ImageField(verbose_name = 'Imagen', upload_to = 'multimedia')
    link = models.URLField(blank = True, null = True, verbose_name = 'Enlace')
    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de modificación')

    class Meta:
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolios'
        ordering = ['-created']

    def __str__(self):
        return self.title
