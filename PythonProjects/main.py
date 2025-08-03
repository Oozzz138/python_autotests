import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '943dca9d601da1f9703bfcf92353ba62'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}

body_creature = {
    "name": "Oozzz",
    "photo_id": 10
}
body_change_the_name = {
    "pokemon_id": "369428",
    "name": "papa",
    "photo_id": 10
}
body_Catch_at_pokeball = {
    "pokemon_id": "369428"
}

response_creature = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creature)
print(response_creature.text)

response_change_the_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_the_name)
print(response_change_the_name.text)


response_Catch_at_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_Catch_at_pokeball)
print(response_Catch_at_pokeball.text)

message = response_creature.json()['message']
print(message)

message = response_change_the_name.json()['message']
print(message)

message = response_Catch_at_pokeball.json()['message']
print(message)