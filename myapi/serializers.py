from rest_framework import serializers
from . import models

# serializers turn models into a JSON representation so that they can be parsed by an API user

class PokedexEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pokedex
        fields = ['pokemon_id','pokemon_name','pokemon_type','pokemon_species','pokemon_height', 'pokemon_weight', 'pokemon_abilities', 'pokemon_entrydate','pokemon_updatedat']