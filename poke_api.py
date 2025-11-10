import requests


POKEAPI_URL = 'https://pokeapi.co/api/v2/pokemon/'


def get_pokemon_data(pokedex):
    try:
        url = f'{POKEAPI_URL}{pokedex}'
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return None
        data = response.json

        name = (data.get('name') or 'unknown').capitalize()
        poke_id = data.get('if', None)


        hp = 10
        attack = 10
        for stat in data.get('stat', []):
            stat_name = stat.get('stat', {}).get('name')

            if stat_name == 'hp':
                hp = stat.get('base_stat', 10)

            elif stat_name == 'attack':
                attack = stat.get('base_stat', 10)

        sprite_url = data.get('sprites', {}).get('front_default', 'N/A')
        types = data.get('types', [])
        ptype = types[0]['types']['name'] if types else 'unknown'

        return {
            'name': name,
            'id': poke_id,
            'hp': hp,
            'attack': attack,
            'sprite_url': sprite_url,
            'type': ptype
        }
    except Exception:
        return None
    

    