from item import itens
from mercado import Caixa

def main():
    caixa1 = Caixa(1)
    caixa2 = Caixa(2)

    carrinho1 = [
        itens['Pano'],
        itens['Pão'],
        itens['Pão'],
        itens['Suco'],
        itens['Suco'],
        itens['Suco'],
        itens['Suco'],
        itens['Sorvete']
    ]

    carrinho2 = [
        itens['Sorvete'],
        itens['Sorvete'],
        itens['Pano']
    ]

    total1 = caixa1.processar_carrinho(carrinho1)
    total2 = caixa2.processar_carrinho(carrinho2)

    print(f'Pessoa 1 vai gastar R$ {total1:.2f}')
    caixa1.finalizar_compra()

    print(f'Pessoa 2 var gastar R$ {total2:.2f}')
    caixa2.finalizar_compra()


if __name__ == '__main__':
    main()
