# Generated by Django 5.1.4 on 2024-12-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('Id_Cliente', models.IntegerField(primary_key=True, serialize=False)),
                ('No_Telefono', models.IntegerField()),
                ('Fecha_Nacimiento', models.DateField()),
                ('Correo', models.CharField(max_length=100)),
                ('Nombre', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=100)),
                ('Sexo', models.CharField(max_length=300)),
            ],
        ),
    ]
