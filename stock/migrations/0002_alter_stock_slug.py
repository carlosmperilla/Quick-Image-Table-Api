# Generated by Django 3.2.18 on 2023-04-28 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='slug',
            field=models.SlugField(default='768b0e04a1fe4ac8891bcedc82a06d1c', unique=True, verbose_name='Nombre unico de stock'),
        ),
    ]