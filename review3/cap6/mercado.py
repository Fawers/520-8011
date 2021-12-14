class Caixa:
    def __init__(self, numero):
        self.numero = numero

    def processar_carrinho(self, itens):
        self.compra = Compra()

        for item in itens:
            self.compra.add_item(item)

        total = self.compra.get_total()
        return total

    def finalizar_compra(self):
        print(self.compra.montar_extrato())

class Compra:
    def __init__(self):
        self.itens = {}

    def add_item(self, item):
        if item in self.itens:
            self.itens[item] += 1

        else:
            self.itens[item] = 1

    def get_total(self):
        total = 0.0

        for (item, qtd) in self.itens.items():
            total += item.preco * qtd

        return total

    def montar_extrato(self):
        cabecalho = f"{'Item':^10} | {'P. Unitário':^12} | {'Quantidade':^12} | {'Preço':^10}"

        total = 0.0
        linhas = []

        for (item, qtd) in self.itens.items():
            preco_cheio = item.preco * qtd
            total += preco_cheio
            linhas.append(f"{item.nome:^10} | {item.preco:^12} | {qtd:^12} | {preco_cheio:^10}")

        linha_total = f"{'Total':^10} | {'':^12} | {'':^12} | {total:^10}"
        linhas_str = '\n'.join(linhas)

        return f"{cabecalho}\n{linhas_str}\n{linha_total}\n"


