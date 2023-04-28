# Generated by Django 3.2.18 on 2023-04-28 09:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='Nombre unico de producto'),
        ),
    ]
