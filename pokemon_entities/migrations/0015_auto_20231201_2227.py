# Generated by Django 3.1.14 on 2023-12-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0014_auto_20231201_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(verbose_name='Появился в'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(verbose_name='Исчез в'),
        ),
    ]
