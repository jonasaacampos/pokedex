# -*- coding: utf-8 -*-

# -- Sheet --

# ##  Pokedex
# Função recebe o nome de um pokemon:
#  - mostra sua ficha pokemon 
#  - baixa a imagem do pokemon e salva no diretorio img/


# ![pikachu](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/25.svg)


def imgDownload(link, name):
    """Função baixa imagem da internet e salva no disco local em formato *.png
    Args:
        link (str): link da sua imagem
        name (str): nome do arquivo a ser salvo
    """
    import urllib.request
    urllib.request.urlretrieve(f"{link}", f"{name}.png")
    #print("download successful")

class Colors:
    """Insere/remove cores da saída do terminal
    """    
    reset_color = '\033[m'
    vermelho = '\033[31m'
    verde = '\033[32m'
    amarelo = '\033[33m'
    azul = '\033[34m'

def espacador():
    """Pula uma linha em branco e insere uma linha decorada na saída do código
    """    
    print()
    print('-*-' * 35)
    print()

def pokedex():
    """Função pede que o usuário entre com o nome de um pokemon qualquer.
        Se o pokemon existir ele exibe sua ficha pokemon e salva sua foto no diretório img
        Caso o pokemon a função trará uma mensagem de erro.
    """    
    import requests
    import json
    

    print('Saiba os dados completos do seu pokemon')
    nome = input('Insira o nome do seu pokemon').lower()
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nome}')
    response_json = response.json()
    espacador()
    
    print(f'{Colors.amarelo}{nome}{Colors.reset_color}')
    #mostra todos os dados do pokemon
    for v in response_json.keys():
        print(f'{v}: {response_json[v]}')

    pokemon_id = response_json['id']
    pokemon_id_str = str(pokemon_id)

    if pokemon_id < 10:
        pokemon_id_str = '0' + pokemon_id_str
    if pokemon_id < 100:
        pokemon_id_str = '0' + pokemon_id_str
    

    img_link = f'https://assets.pokemon.com/assets/cms2/img/pokedex/full/{pokemon_id_str}.png'
    file_folder = 'img/'

    file_name = file_folder + nome
    imgDownload(img_link, file_name)

pokedex()

