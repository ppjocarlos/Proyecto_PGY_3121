# Generated by Django 4.2.1 on 2023-07-08 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0009_alter_noticia_informacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='informacion',
            field=models.TextField(null=True),
        ),
    ]
