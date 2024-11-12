from django.urls import path
from . import views

app_name = 'cartelera'

urlpatterns = [
    path('peliculas/', views.listar_peliculas, name='listar_peliculas'),
    path('peliculas/agregar/', views.agregar_pelicula, name='agregar_pelicula'),
    path('peliculas/eliminar/<int:id_pelicula>/', views.eliminar_pelicula, name='eliminar_pelicula'),   
    path('proyecciones/<str:proyeccion_id>/reservar/', views.reservar_boleto, name='reservar_boleto'),
]
