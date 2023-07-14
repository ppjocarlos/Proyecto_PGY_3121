# Generated by Django 4.2.1 on 2023-06-17 14:47

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
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('tipo_contacto', models.IntegerField(choices=[[0, 'Sugerencia'], [1, 'Reclamo'], [2, 'Felicitaciones']])),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Periodista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
                ('telefono', models.IntegerField()),
                ('profesion', models.CharField(max_length=80)),
                ('correo', models.EmailField(max_length=254)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
                ('informacion', models.TextField()),
                ('foto', models.ImageField(null=True, upload_to='noticias')),
                ('periodista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appweb.periodista')),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appweb.seccion')),
            ],
        ),
    ]