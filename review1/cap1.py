def ex1():
    nome = input('Digite o seu nome: ')
    idade = input('Digite a sua idade: ')
    idade = int(idade)
    #idade = int(input('Digite a sua idade: '))
    # int('29')
    maior = input('Você é maior de idade? [s/n] ').strip().lower() == 's'
    # maior = input('Você é maior de idade? [s/n] ')
    # maior = maior.strip()
    # maior = maior.lower()
    # maior = maior == 's'

    print('-' * 20)
    print("Dados entrados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Maior de idade: {maior}")
    print('-' * 20)


def ex2(frase, termo, sub):
    # frase = "Umxpratoxdextrigoxparaxtrêsxtigresxtristes"
    # termo_substituicao = 'x'
    # substituidor = '$'

    print(frase.replace(termo, sub))
    # print(frase ,termo_substituicao, substituidor)
    # print("Umxpratoxdextrigoxparaxtrêsxtigresxtristes")


def ex3(a, b):
    so = a + b
    su = a - b
    mu = a * b
    di, re = divmod(a, b)
    # res = divmod(a, b)
    # di = res[0]
    # re = res[1]

    return so, su, mu, di, re


# ex1()
# ex2("Umxpratoxdextrigoxparaxtrêsxtigresxtristes", 'X'.lower(), ' ')
print(ex3(int(input('Digite o primeiro num: ')),
          int(input('Digite o segundo num: '))))
