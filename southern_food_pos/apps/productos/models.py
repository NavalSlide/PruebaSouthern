from django.db import models
from django.conf import settings

# Modelo para la categoría de productos
class Categoria(models.Model):
    # Nombre de la categoría, máximo 100 caracteres
    nombre = models.CharField(max_length=100)
    # Descripción de la categoría, opcional
    descripcion = models.TextField(blank=True)
    # Relación con el usuario que creó la categoría
    usuario_creador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        related_name='categorias', 
        null=True
    )
    
    # Representación en cadena del objeto
    def __str__(self):
        return self.nombre

    class Meta:
        # Nombre singular para la interfaz de administración
        verbose_name = "Categoría"
        # Nombre plural para la interfaz de administración
        verbose_name_plural = "Categorías"

# Modelo para los productos
class Producto(models.Model):
    # Nombre del producto, máximo 100 caracteres
    nombre = models.CharField(max_length=100)
    # Precio del producto, con hasta 10 dígitos y 2 decimales
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # Descripción detallada del producto
    descripcion = models.TextField(blank=True)  # Hacerlo opcional
    # Cantidad en stock, solo valores enteros positivos
    stock = models.PositiveIntegerField(default=0)
    # Imagen del producto, se guarda en la carpeta 'productos/'
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  # Hacerlo opcional
    # Código de barras del producto, opcional
    codigo_barras = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name="Código de barras"
    )  # Añadido campo de código de barras
    # Relación con la categoría, permite valor nulo
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    # Fecha de creación del producto, se establece automáticamente
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # Relación con el usuario que creó el producto
    usuario_creador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        related_name='productos', 
        null=True
    )

    # Representación en cadena del objeto
    def __str__(self):
        return self.nombre

