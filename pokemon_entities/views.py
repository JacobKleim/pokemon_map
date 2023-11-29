import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from pokemon_entities.models import Pokemon, PokemonEntity

from django.utils.timezone import localtime


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons_entity = PokemonEntity.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entity:
        if pokemon_entity.appeared_at <= localtime() <= pokemon_entity.disappeared_at:
            image_url = request.build_absolute_uri(pokemon_entity.pokemon.image.url)
            add_pokemon(
                folium_map, pokemon_entity.lat,
                pokemon_entity.lon,
                image_url
            )

    pokemons_on_page = Pokemon.objects.all()

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon_entity = PokemonEntity.objects.get(pokemon=pokemon)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    image_url = request.build_absolute_uri(pokemon_entity.pokemon.image.url)
    pokemon_data = {
        'lat': pokemon_entity.lat,
        'lon': pokemon_entity.lon,
        'img_url': image_url,
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description
    }
    add_pokemon(
        folium_map, pokemon_data['lat'],
        pokemon_data['lon'],
        pokemon_data['img_url']
    )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_data
    })


# pokemon = Pokemon.objects.get(id=pokemon_id)
#     pokemon_entity = PokemonEntity.objects.get(pokemon=pokemon)
#     folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
#     image_url = request.build_absolute_uri(pokemon_entity.pokemon.image.url)
#     add_pokemon(
#         folium_map, pokemon_entity.lat,
#         pokemon_entity.lon,
#         image_url
#     )