# Generated by Django 5.0.4 on 2024-04-11 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_favorite_favoriteitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoriteitem',
            name='product_name',
        ),
    ]