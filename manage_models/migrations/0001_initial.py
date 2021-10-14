# Generated by Django 3.2.8 on 2021-10-14 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=3)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo_electronico', models.EmailField(max_length=254, null=True)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo_electronico', models.EmailField(max_length=254, null=True)),
                ('telefono', models.CharField(max_length=10)),
                ('tipo_usuario', models.CharField(choices=[('A', 'ADMINISTRADOR'), ('V', 'VENDEDOR')], max_length=1)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_venta', models.DateTimeField(auto_now_add=True)),
                ('caja', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manage_models.caja')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manage_models.cliente')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manage_models.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=6)),
                ('categoria', models.ManyToManyField(blank=True, null=True, to='manage_models.Categoria')),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='manage_models.marca')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=6)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=6)),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manage_models.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_models.venta')),
            ],
        ),
        migrations.CreateModel(
            name='CorteCaja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('fecha_cierre', models.DateTimeField(blank=True, null=True)),
                ('saldo_inicial', models.DecimalField(decimal_places=2, max_digits=6)),
                ('saldo_final', models.DecimalField(decimal_places=2, max_digits=6)),
                ('estado', models.CharField(choices=[('A', 'Abierta'), ('C', 'Cerrada')], max_length=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manage_models.usuario')),
            ],
        ),
    ]
