# Generated by Django 3.1.6 on 2021-04-29 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20210428_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokedex',
            name='pokemon_entrydate',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Entry'),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='pokemon_updatedat',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
    ]