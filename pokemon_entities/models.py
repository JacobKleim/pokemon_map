from django.db import models 

from datetime import datetime

class Pokemon(models.Model):
    title = models.CharField(verbose_name='Название на русском', 
                             max_length=200)
    title_en = models.CharField(verbose_name='Название на английском', 
                                max_length=200,
                                blank=True, null=True)
    title_jp = models.CharField(verbose_name='Название на японском',
                                max_length=200, blank=True, null=True)
    previous_evolution = models.ForeignKey('self',
                                           verbose_name='Из кого эволюционирует',
                                           null=True,
                                           blank=True,
                                           related_name='next_evolutions',
                                           on_delete=models.SET_NULL)
    description = models.TextField(verbose_name='Описание', 
                                   blank=True, null=True)
    image = models.ImageField(verbose_name='Изображение',
                              blank=True, null=True)
    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, 
                                verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(default=datetime(2023, 1, 2), 
                                       verbose_name='Появился в')
    disappeared_at = models.DateTimeField(default=datetime(2023, 1, 2), 
                                          verbose_name='Исчез в')
    level = models.IntegerField(blank=True, null=True, 
                                verbose_name='Уровень')
    health = models.IntegerField(blank=True, null=True, 
                                 verbose_name='Здоровье')
    strenght = models.IntegerField(blank=True, null=True, 
                                   verbose_name='Сила')
    defence = models.IntegerField(blank=True, null=True, 
                                  verbose_name='Защита')
    stamina = models.IntegerField(blank=True, null=True, 
                                  verbose_name='Выносливость')
    
    class Meta:
        verbose_name = 'Экземпляр покемона'
        verbose_name_plural = 'Экземпляры покемона'
    
    