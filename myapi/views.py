from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PokedexEntrySerializer
from .models import Pokedex
from rest_framework import filters

class PokedexEntryViewSet(viewsets.ModelViewSet):
    search_fields = ['pokemon_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Pokedex.objects.all().order_by('pokemon_name')
    serializer_class = PokedexEntrySerializer