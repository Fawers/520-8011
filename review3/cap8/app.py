from banco import item

def main():
    item.criar_tabela()

    for (nome, preco) in [('detergente', 5), ('sabão', 5), ('esponja', 3)]:
        item.inserir_item(nome, preco)

    print(item.selecionar_itens(5))

if __name__ == '__main__':
    main()
