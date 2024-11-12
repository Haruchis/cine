from django.db import models

# Create your models here.
from django.db import models

class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)

    def _str_(self):
        return self.nombre

class Empleado(models.Model):
    id_empleado = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre

class Sala(models.Model):
    id_sala = models.CharField(primary_key=True, max_length=50)
    numero_sala = models.CharField(max_length=5)
    capacidad = models.IntegerField()

    def _str_(self):
        return f"Sala {self.numero_sala}"


class Proyeccion(models.Model):
    id_pelicula = models.ForeignKey(
        'Pelicula',  # Referencia entre comillas
        on_delete=models.CASCADE,
        related_name='proyecciones'
    )
    fecha = models.DateField(verbose_name="Fecha")
    hora = models.TimeField(verbose_name="Hora")
    sala = models.CharField(max_length=10, verbose_name="Sala")

    def __str__(self):
        return f"{self.id_pelicula.titulo} - {self.fecha} {self.hora}"




class Venta(models.Model):
    id_venta = models.CharField(primary_key=True, max_length=50)
    fecha = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def _str_(self):
        return f"Venta {self.id_venta} por {self.total}"

class Boleto(models.Model):
    id_boleto = models.CharField(primary_key=True, max_length=50)
    asiento = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_proyeccion = models.ForeignKey(Proyeccion, on_delete=models.CASCADE)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)

    def _str_(self):
        return f"Boleto {self.id_boleto} - Asiento {self.asiento}"
    
class Pelicula(models.Model):
    id_pelicula = models.AutoField(primary_key=True) 
    titulo = models.CharField(max_length=100, unique=True, verbose_name="Título")
    genero = models.CharField(max_length=50, verbose_name="Género")
    clasificacion = models.CharField(max_length=10, verbose_name="Clasificación")
    duracion = models.PositiveIntegerField(verbose_name="Duración (min)")
    sinopsis = models.TextField(verbose_name="Sinopsis", blank=True, null=True)
    fecha_estreno = models.DateField(verbose_name="Fecha de Estreno", blank=True, null=True)
    imagen = models.ImageField(upload_to='imagenes_peliculas/', blank=True, null=True, verbose_name="Imagen de la Película")

    class Meta:
        ordering = ['titulo']
        verbose_name = "Película"
        verbose_name_plural = "Películas"

    def __str__(self):
        return self.titulo
