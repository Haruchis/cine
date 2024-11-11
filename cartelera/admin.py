from django.contrib import admin
from .models import Cliente, Empleado, Sala, Pelicula, Proyeccion, Venta, Boleto

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Sala)
admin.site.register(Pelicula)
admin.site.register(Proyeccion)
admin.site.register(Venta)
admin.site.register(Boleto)