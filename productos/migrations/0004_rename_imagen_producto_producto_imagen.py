# Generated by Django 5.0.4 on 2025-03-03 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_producto_imagen_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='imagen_producto',
            new_name='imagen',
        ),
    ]
