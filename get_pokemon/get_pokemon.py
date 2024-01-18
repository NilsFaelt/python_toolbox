"""Fetching Pokemons from api"""
import json
import httpx

async def get_pokemon(pokemon_name=None):
    """Fetching pokemons"""
    try:
        if not pokemon_name:
            url = "https://pokeapi.co/api/v2/pokemon/ditto"
        else:
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status() 
            parsed_data = json.loads(response.text)
            pokemon_name = parsed_data['name']
            abilities = [ability['ability']['name'] for ability in parsed_data['abilities']]
            print(f" Name: {pokemon_name} Abilities: {', '.join(abilities)} ")
            return response.text
    except httpx.HTTPError as e:
        print(f"Error fetching Pokemon data: {e}")
        return None
