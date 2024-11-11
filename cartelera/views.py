from django.shortcuts import get_object_or_404

from django.shortcuts import render
from .models import Pelicula, Proyeccion

def listar_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'cartelera/listar_peliculas.html', {'peliculas':peliculas})
                                                               
def ver_proyecciones(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id_pelicula=pelicula_id)
    proyecciones = Proyeccion.objects.filter(id_pelicula=pelicula)
    return render(request, 'cartelera/ver_proyecciones.html', {'pelicula': pelicula, 'proyecciones':proyecciones})
                                                               

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Boleto, Cliente

def reservar_boleto(request, proyeccion_id):
    if request.method == 'POST':
        asiento = request.POST['asiento']
        cliente_id = request.POST['cliente_id']
        cliente = get_object_or_404(Cliente, id_cliente=cliente_id)
        proyeccion = get_object_or_404(Proyeccion, id_proyeccion=proyeccion_id)
        
        # Crear un nuevo boleto
        boleto = Boleto(asiento=asiento, precio=10.00, id_cliente=cliente, id_proyeccion=proyeccion)
        boleto.save()
        
        return HttpResponseRedirect(reverse('cartelera:ver_proyecciones', args=[proyeccion.id_pelicula.id_pelicula]))

    return render(request, 'cartelera/reservar_boleto.html', {'proyeccion_id':proyeccion_id})                                                              