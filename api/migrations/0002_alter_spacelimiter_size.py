# Generated by Django 3.2.18 on 2023-04-29 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spacelimiter',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]
