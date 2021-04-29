from django.db import models
from datetime import datetime   

class Pokedex(models.Model):
    pokemon_id = models.AutoField(primary_key=True)
    pokemon_name = models.TextField(max_length=255)
    pokemon_type = models.CharField(max_length=50)
    pokemon_species = models.TextField(max_length=50)
    pokemon_height = models.DecimalField(max_digits=13,decimal_places=2)
    pokemon_weight = models.DecimalField(max_digits=13,decimal_places=2)
    pokemon_abilities = models.TextField(max_length=255)
    pokemon_entrydate = models.DateTimeField('Date Entry', auto_now=True, blank=False)
    pokemon_updatedat = models.DateTimeField('Updated At',auto_now=True, blank=False)
    def __str__(self):
        return self.pokemon_name