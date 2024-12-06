# Generated by Django 5.1.4 on 2024-12-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('Id_Empleados', models.IntegerField(primary_key=True)),
                ('Nombre', models.CharField(max_length=100)),
                ('No_Telefono', models.IntegerField()),
                ('Correo', models.CharField(max_length=100)),
                ('Fecha_Nacimiento', models.DateTimeField()),
                ('Salario', models.IntegerField()),
                ('Direccion', models.CharField(max_length=300)),
            ],
        ),
    ]