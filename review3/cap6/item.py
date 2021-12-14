class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f"Item({self.nome}, R$ {self.preco:.2f})"


itens = {
    'Pano': Item('pano', 1.0),
    'Suco': Item('suco', 3.0),
    'Pão': Item('pão', 5.0),
    'Sorvete': Item('sorvete', 10.0)
}
