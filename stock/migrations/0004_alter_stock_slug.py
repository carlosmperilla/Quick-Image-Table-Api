# Generated by Django 3.2.18 on 2023-04-28 09:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_alter_stock_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='slug',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]