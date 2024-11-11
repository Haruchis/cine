from django.urls import path
from . import views

app_name = 'cartelera'

urlpatterns = [
    path('peliculas/', views.listar_peliculas, name='listar_peliculas'),
    path('peliculas/agregar/', views.agregar_pelicula, name='agregar_pelicula'),  # Nueva URL para agregar películas
    path('proyecciones/<str:proyeccion_id>/reservar/', views.reservar_boleto, name='reservar_boleto'),
]
