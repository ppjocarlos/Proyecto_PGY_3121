# Generated by Django 4.2.1 on 2023-07-08 01:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0008_alter_noticia_mensaje_rechazo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='informacion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='mensaje_rechazo',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
