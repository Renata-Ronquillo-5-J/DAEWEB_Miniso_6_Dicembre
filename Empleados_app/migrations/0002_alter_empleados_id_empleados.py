# Generated by Django 5.1.4 on 2024-12-06 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='Id_Empleados',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
