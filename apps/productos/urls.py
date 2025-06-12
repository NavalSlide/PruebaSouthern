from django.urls import path
from . import views

# Define el espacio de nombres para la aplicación
app_name = 'productos'

# Patrones de URL para las vistas de la aplicación
urlpatterns = [
    # Ruta para la lista de productos
    path('', views.lista_productos, name='lista'),
    # Ruta para crear un nuevo producto
    path('nuevo/', views.crear_producto, name='crear'),
    # Ruta para editar un producto existente, usando el ID (pk)
    path('editar/<int:pk>/', views.editar_producto, name='editar'),
    # Ruta para eliminar un producto, usando el ID (pk)
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar'),
    # Ruta para crear una nueva categoría
    path('categorias/nueva/', views.crear_categoria, name='categoria_create'),
    # Ruta para buscar productos
    path('buscar/', views.buscar_productos, name='buscar'),
    path('api/buscar-por-codigo/', views.buscar_producto_por_codigo, name='buscar_por_codigo'),
]