import json
import random


nomes = {}


def carregar(arquivo='nomes.json'):
    global nomes

    with open(arquivo) as a:
        nomes = json.load(a)


def gerar():
    primeiro = random.choice(nomes['nomes'])
    ultimo = random.choice(nomes['sobrenomes'])

    return f"{primeiro} {ultimo}"


carregar()
