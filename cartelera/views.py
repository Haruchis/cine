from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Pelicula, Proyeccion, Boleto, Cliente
from .forms import PeliculaForm

def listar_peliculas(request):
    """
    Vista para listar todas las películas disponibles y manejar la creación de nuevas películas.
    """
    peliculas = Pelicula.objects.all()
    
    # Crear un formulario vacío en caso de que se necesite en el modal
    form = PeliculaForm()
    
    # Si se envía el formulario para agregar una película (método POST)
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cartelera:listar_peliculas')
    
    return render(request, 'cartelera/listar_peliculas.html', {
        'peliculas': peliculas,
        'form': form
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
