# Generated by Django 5.1.4 on 2024-12-17 16:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('codigo', models.CharField(max_length=10)),
                ('categoria', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img/productos')),
                ('descuento', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_publicacion', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
