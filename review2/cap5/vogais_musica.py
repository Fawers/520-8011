def carregar_letra(arquivo='help.txt'):
    with open(arquivo) as a:
        letra = a.read()

    return letra

def contar_vogais_maiusculas_e_minusculas(letra: str):
    vs = 'AEIOUaeiou'
    freqs = {}

    for v in vs:
        freqs[v] = letra.count(v)

    return freqs

def contar_vogais(letra):
    vs = 'aeiou'
    freqs = {}

    for v in vs:
        freqs[v] = 0

    letra = letra.lower()

    for car in letra:
        if car in vs:
            freqs[car] += 1

    return freqs

def main():
    letra = carregar_letra()
    vogais = contar_vogais_maiusculas_e_minusculas(letra)

    print(vogais)


if __name__ == '__main__':
    main()
