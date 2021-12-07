import os.path
import csv


ARQUIVO_CSV = "registros.csv"
CABECALHO_CSV = ["Nome", "GitHub", "NumRepositorios"]


def criar():
    if not os.path.exists(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, 'w') as a:
            writer = csv.writer(a)
            writer.writerow(CABECALHO_CSV)

    dados = []
    for dado in CABECALHO_CSV:
        dados.append(input(f"Digite [{dado}]: "))

    with open(ARQUIVO_CSV, 'a') as a:
        writer = csv.writer(a)
        writer.writerow(dados)


def consultar():
    busca = input("Digite nome ou github a buscar: ").lower()

    with open(ARQUIVO_CSV) as a:
        a = csv.reader(a)
        next(a)

        for (nome, github, _) in a:
            if busca in nome.lower() or busca == github.lower():
                return (nome, github)

        return ()

def excluir():
    pass

def main():
    print("O que vc deseja fazer?")
    print("1 - Criar registro")
    print("2 - Consultar registro")
    # print("3 - Excluir dos registros")
    escolha = input('Digite um número: ')

    if escolha not in '12':
        print("Escolha inválida")

    elif escolha == '1':
        criar()

    elif escolha == '2':
        print(consultar())

    elif escolha == '3':
        excluir()


if __name__ == '__main__':
    main()
