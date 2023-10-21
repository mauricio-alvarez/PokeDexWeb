import requests
import json
from PIL import Image

api = "https://pokeapi.co/api/v2/"

def getEvolution(link):
    response = requests.get(link)
    dataextra = response.json()
    data = {}
    data['EVO1'] = (dataextra['chain']['species'])
    if dataextra['chain']['evolves_to'] != []:
        data['EVO2'] = (dataextra['chain']['evolves_to'][0]['species'])
        if dataextra['chain']['evolves_to'] != []:
            data['EVO3'] = (dataextra['chain']['evolves_to'][0]['evolves_to'][0]['species'])
    
    return data
    
    o
def getPicture(pokename):
    return (f'PokemonDataset/{pokename}.png')


def getforname(pokemon_name):
    data1 = f"{api}pokemon/{pokemon_name}/"
    data2 = f"{api}pokemon-species/{pokemon_name}/"
    
    try:
        response = (requests.get(data1), requests.get(data2))
        response[0].raise_for_status()
        response[1].raise_for_status()
        pokemon_data = response[0].json()
        pokemon_data.update(response[1].json())
        return pokemon_data
    except requests.exceptions.RequestException as e:
        print('El pokemon no existe o aun no lo conozco')
        print(e)
