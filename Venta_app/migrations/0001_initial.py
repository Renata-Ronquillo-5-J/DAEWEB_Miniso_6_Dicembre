# Generated by Django 5.1.4 on 2024-12-06 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('Id_Venta', models.IntegerField(primary_key=True, serialize=False)),
                ('Id_Empleado', models.IntegerField()),
                ('Id_Producto', models.IntegerField()),
                ('NombreProducto', models.CharField(max_length=300)),
                ('Cantidad', models.IntegerField()),
                ('Total', models.IntegerField()),
                ('FechaVenta', models.DateField()),
            ],
        ),
    ]