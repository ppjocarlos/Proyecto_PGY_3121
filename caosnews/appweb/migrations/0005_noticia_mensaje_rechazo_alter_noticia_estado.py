# Generated by Django 4.2.1 on 2023-06-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0004_noticia'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='mensaje_rechazo',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='estado',
            field=models.IntegerField(choices=[[0, 'En Espera'], [1, 'Aprobado'], [2, 'Rechazado']], default=0),
        ),
    ]
