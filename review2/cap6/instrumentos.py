class InstrumentoDeCorda:
    SEQUENCIA = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#',
                 'G', 'G#', 'A', 'A#', 'B')

    def __init__(self, *afinacao_cordas):
        # exemplo afinacao_cordas:
        # ['E', 'A', 'D', 'G', 'B', 'E']
        self.cordas = afinacao_cordas

    def __repr__(self):
        return f"{self.__class__.__name__} {self.cordas}"

    def acorde(self, *posicoes):
        assert len(posicoes) == len(self.cordas)
        notas = list(self.cordas)

        for (i, p) in enumerate(posicoes):
            index_seq = self.SEQUENCIA.index(notas[i])
            novo_index = index_seq + p
            index_nota = novo_index % len(self.SEQUENCIA)
            notas[i] = self.SEQUENCIA[index_nota]

        return notas

    def pestana(self, posicao):
        notas = list(self.cordas)

        for i in range(len(notas)):
            index_seq = self.SEQUENCIA.index(notas[i])
            novo_index = index_seq + posicao
            index_nota = novo_index % len(self.SEQUENCIA)
            notas[i] = self.SEQUENCIA[index_nota]

        return notas

class Violao(InstrumentoDeCorda):
    def __init__(self):
        super().__init__('E', 'A', 'D', 'G', 'B', 'E')

class Guitarra7(InstrumentoDeCorda):
    def __init__(self):
        super().__init__('B', 'E', 'A', 'D', 'G', 'B', 'E')

class Baixo(InstrumentoDeCorda):
    def __init__(self):
        super().__init__('E', 'A', 'D', 'G')
