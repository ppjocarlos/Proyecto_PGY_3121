# Generated by Django 4.2.1 on 2023-07-14 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0010_alter_noticia_informacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='fecha2',
            field=models.DateField(null=True),
        ),
    ]
