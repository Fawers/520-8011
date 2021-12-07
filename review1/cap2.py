def ep1():  # explicação 1
    nota1, nota2, nota3 = 5, 5, 5
    media = (nota1 + nota2 + nota3) / 3
    print(media)

    if media >= 6:
        print('aprovado')

    elif media >= 4.5:
        print('recuperação')

    # else:
    #     print('reprovado')

def ep2(inicio=10):
    contagem = inicio

    while contagem > 0:
        if contagem % 2 == 0:
            print(contagem)
        if contagem == 4:
            break
        contagem -= 1
        # contagem = contagem - 1
    print('fim do loop')


def ep3(seq=range(0,10)):
    for item in seq:
        print(item)

def ep4():
    lista = [5,6,7,8]
    tupla = (1,2,3)

    lista.append(9)
    lista.insert(0, 4)
    lista.append(tupla)
    print(lista)
    print(lista[3])
    print(lista[1:4])
    print()
    print(tupla)
    print(tupla[1])
    print(tupla[1:2])

    for num in tupla:
        print(num)


def ep5():
    curso = {
        'nome': 'Python Fundamentals',
        'id': 520,
        'turmas': {
            8011: {
                'estudantes': [
                    'Fernando', 'Joao', 'Rubens', 'Douglas'
                ]
            }
        }
    }

    curso['turmas'][8011]['estudantes'].append('Fabricio')
    # turmas = curso['turmas']
    # turma = turmas[8011]
    # estudantes = turma['estudantes']
    # estudantes.append('Fabricio')
    print(f"Curso {curso['id']} {curso['nome']}")
    print(curso['turmas'][8011]['estudantes'])


def ex1(ano):
    geracoes = {
        1964: 'Baby Boomer',
        1979: 'Gen X',
        1994: 'Gen Y'
    }

    for (ano_piso, gen) in geracoes.items():
        if ano <= ano_piso:
            return gen
    return 'Gen Z'

def fn(*args):
    print(args)

def kwfn(**kwargs):
    print(kwargs)
    print(kwargs['nome'])

# print(ex1(ano=int(input('Entre com o ano de nascimento: '))))

# fn(1, 2, 'nome', 3.4, [3,4], {1: 'um'})
kwfn(nome='Fabricio', ano=1992)
