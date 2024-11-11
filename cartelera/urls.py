from django.urls import path
from . import views

app_name = 'cartelera'

urlpatterns = [
    path('peliculas/', views.listar_peliculas, name='listar_peliculas'),
    path('peliculas/<str:pelicula_id>/proyecciones/', views.ver_proyecciones, name='ver_proyecciones'),
    path('proyecciones/<str:proyeccion_id>/reservar/', views.reservar_boleto, name='reservar_boleto'),
]