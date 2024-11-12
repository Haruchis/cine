from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Pelicula, Proyeccion, Boleto, Cliente
from .forms import PeliculaForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def listar_peliculas(request):
    """
    Vista para listar todas las películas disponibles.
    Solo los administradores pueden agregar y eliminar películas.
    """
    peliculas = Pelicula.objects.all()
    form = PeliculaForm() if request.user.is_staff else None  # Solo carga el formulario para el admin

    if request.method == 'POST' and request.user.is_staff:
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cartelera:listar_peliculas')

    return render(request, 'listar_peliculas.html', {
        'peliculas': peliculas,
        'form': form,
        'es_admin': request.user.is_staff,  # Pasar si es admin
    })


def agregar_pelicula(request):
    """
    Vista para agregar una nueva película.
    """
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cartelera:listar_peliculas')
    else:
        form = PeliculaForm()

    return render(request, 'cartelera/agregar_pelicula.html', {'form': form})
def ver_proyecciones(request, pelicula_id):
    """
    Vista para mostrar las proyecciones disponibles de una película específica.
    """
    pelicula = get_object_or_404(Pelicula, id_pelicula=pelicula_id)
    proyecciones = Proyeccion.objects.filter(id_pelicula=pelicula)
    return render(request, 'cartelera/ver_proyecciones.html', {
        'pelicula': pelicula,
        'proyecciones': proyecciones
    })

def reservar_boleto(request, proyeccion_id):
    """
    Vista para reservar un boleto para una proyección específica.
    """
    proyeccion = get_object_or_404(Proyeccion, id_proyeccion=proyeccion_id)

    if request.method == 'POST':
        asiento = request.POST.get('asiento')
        cliente_id = request.POST.get('cliente_id')
        cliente = get_object_or_404(Cliente, id_cliente=cliente_id)

        # Crear y guardar el nuevo boleto
        boleto = Boleto(
            asiento=asiento,
            precio=10.00,  # Puedes modificar el precio si es necesario
            id_cliente=cliente,
            id_proyeccion=proyeccion
        )
        boleto.save()

        # Redirigir de regreso a la lista de proyecciones de la película
        return HttpResponseRedirect(reverse('cartelera:ver_proyecciones', args=[proyeccion.id_pelicula.id_pelicula]))

    return render(request, 'cartelera/reservar_boleto.html', {
        'proyeccion': proyeccion
    })
# views.py
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def eliminar_pelicula(request, id_pelicula):
    pelicula = get_object_or_404(Pelicula, id_pelicula=id_pelicula)
    pelicula.delete()
    return redirect('cartelera:listar_peliculas')

