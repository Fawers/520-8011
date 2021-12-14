try:
    idade = int(input('Qual é a sua idade? '))
    print(f'Vc tem {idade} anos')
    idade + 'bla'
    idade / 0

except ValueError as ve:
    print('Não é um número:', ve.args[0])

except ZeroDivisionError:
    print('divisão por zero')

except TypeError:
    print("somar inteiro e string não rola")

except Exception as e:
    print('ocorreu algum problema:', e.__class__)

print('Execução continuou normalmente')
