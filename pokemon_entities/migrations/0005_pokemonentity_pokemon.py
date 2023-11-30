# Generated by Django 3.1.14 on 2023-11-27 18:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_pokemonentity'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon'),
            preserve_default=False,
        ),
    ]
