# Generated by Django 3.2.8 on 2024-11-11 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('puesto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id_pelicula', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('duracion', models.CharField(max_length=10)),
                ('genero', models.CharField(max_length=50)),
                ('clasificacion', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id_sala', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('numero_sala', models.CharField(max_length=5)),
                ('capacidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cartelera.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Proyeccion',
            fields=[
                ('id_proyeccion', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('id_pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cartelera.pelicula')),
                ('id_sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cartelera.sala')),
            ],
        ),
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('id_boleto', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('asiento', models.CharField(max_length=10)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cartelera.cliente')),
                ('id_proyeccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cartelera.proyeccion')),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cartelera.venta')),
            ],
        ),
    ]
