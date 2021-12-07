import time
import random

import name_generator as ng


def contagem(msg='Iniciando em', inicio=3):
    delay = 1

    print(f"{msg} {inicio}...", end=' ', flush=True)
    time.sleep(delay)

    for c in range(inicio-1, 0, -1):
        print(f"{c}...", end=' ', flush=True)
        time.sleep(delay)


def jogar(num_partipantes=10):
    participantes = []

    for _ in range(num_partipantes):
        participantes.append(ng.gerar())

    print("Participantes:", participantes)
    print("Iniciando jogo...")

    while len(participantes) > 1:
        # escolher aleatoriamente alguém para "perder"
        contagem('Parando a música em')
        sorteado = random.randint(0, len(participantes)-1)
        jogador = participantes.pop(sorteado)
        print(f"{jogador} ficou sem cadeira!")
        print("Jogadores restantes:", len(participantes))

    ganhador = participantes.pop()
    print(f"{ganhador} ganhou o jogo!")
