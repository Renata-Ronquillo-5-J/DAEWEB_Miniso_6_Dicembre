# Generated by Django 5.1.4 on 2024-12-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('Id_Sucursal', models.IntegerField(primary_key=True, serialize=False)),
                ('Ubicacion', models.CharField(max_length=300)),
                ('Correo', models.CharField(max_length=100)),
                ('Telefono', models.IntegerField()),
                ('Ciudad', models.CharField(max_length=300)),
                ('Estado', models.CharField(max_length=300)),
                ('Horario', models.CharField(max_length=300)),
            ],
        ),
    ]