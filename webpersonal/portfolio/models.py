from django.db import models

# Create your models here.


class Project (models.Model):
    title = models.CharField(max_length=200, verbose_name='título')
    description = models.TextField(verbose_name='descripción')
    # Para especificar un sub directorio dentro del default general
    # se usa upload_to
    images = models.ImageField(verbose_name='imagen', upload_to='projects')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Fecha creación')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Fecha modificación')
    moreInformation = models.URLField(null=True, blank=True,
                                      verbose_name='Link más información')

    # Para adicionar metada datos a la clase se debe crear una subclases
    class Meta:
        # Se adicionan atributos especiales para que el administrador
        # tenga esas descripciones
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        # Por defecto ordena ascendentemente, para hacerlo desce se pone
        # configuraciones antes del nombre del campo
        ordering = ['-created']

    # Para adicionar un campo identificador en la pantalla del administrador
    # Se debe sobreescribir el metodo str
    def __str__(self):
        return self.title
