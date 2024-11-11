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

class Pelicula(models.Model):
    id_pelicula = models.CharField(primary_key=True, max_length=50)
    titulo = models.CharField(max_length=200)
    duracion = models.CharField(max_length=10)
    genero = models.CharField(max_length=50)
    clasificacion = models.CharField(max_length=10)

    def _str_(self):
        return self.titulo

class Proyeccion(models.Model):
    id_proyeccion = models.CharField(primary_key=True, max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    id_pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.id_pelicula} en Sala {self.id_sala} a las {self.hora}"

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