# Generated by Django 4.2.1 on 2023-06-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='estado',
            field=models.TextField(default='creado'),
        ),
    ]
