import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e2a8b107b9c77a3d83d326f421b0ba0f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_sozdanie = {
    "name": "Jade",
    "photo_id": 1
}
body_smena_name = {
    "pokemon_id": "286747",
    "name": "Jadeeee",
    "photo_id": 2
}

body_inpokeball = {
    "pokemon_id": "286747"
}

response_sozdanie = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body_sozdanie)
print(response_sozdanie.text)
message = response_sozdanie.json()['message']
print(message)

response_smena_name = requests.put(url=f'{URL}/pokemons', headers = HEADER, json = body_smena_name)
print(response_smena_name.text)
message = response_smena_name.json()['message']
print(message)

response_inpokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_inpokeball)
print(response_inpokeball.text)
message = response_inpokeball.json()['message']
print(message)