from django.test import Client, TestCase
from django.urls import reverse
from .models import Pokedex
from datetime import datetime 
from http import HTTPStatus

class PokedexTest(TestCase):
    def setUp(self):
        pass
    
    def test_create_model(self):
        print("Creating a new pokemon...")
        self.post = Pokedex.objects.create(
            pokemon_name='Pokemon Test  Case',
            pokemon_type='Test',
            pokemon_species='Mouse Test',
            pokemon_height='10',
            pokemon_weight='50',
            pokemon_abilities='Static'
        )

    def test_update_model(self):
        print("Updating a pokemon...")
        self.post = Pokedex.objects.update(
            pokemon_name='Pokemon Test  Case 2',
            pokemon_type='Test 2',
            pokemon_species='Mouse Test 2',
            pokemon_height='10',
            pokemon_weight='50',
            pokemon_abilities='Static'
        )

    def test_create_http(self):
        print("Creating Pokemon using API")
        response = self.client.post("/pokemons/",data={
            "pokemon_name": "Pikachu test",
            "pokemon_type": "Electric",
            "pokemon_species": "Mouse",
            "pokemon_height": "30",
            "pokemon_weight": "10",
            "pokemon_abilities": "Static"
        })
        self.assertEqual(response.status_code, HTTPStatus.CREATED)