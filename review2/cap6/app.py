import instrumentos


def main():
    violao = instrumentos.Violao()
    print(violao)

    print(violao.acorde(0, 3, 2, 0, 1, 0))
    print(violao.pestana(5))

    guitarra = instrumentos.Guitarra7()
    baixo = instrumentos.Baixo()

    print(guitarra)
    print(guitarra.acorde(1, 0, 3, 2, 0, 1, 0))

    print(baixo)
    print(baixo.acorde(0, 2, 2, 1))

if __name__ == '__main__':
    main()
