from .base import abrir_conexao

TABELA = 'itens'

def criar_tabela():
    query = f"""
    CREATE TABLE IF NOT EXISTS {TABELA} (
        nome TEXT,
        preco REAL
    );
    """
    con = abrir_conexao()
    con.execute(query)
    con.commit()
    con.close()


def inserir_item(nome, preco):
    query = f"""
    INSERT INTO {TABELA} values (?, ?);
    """

    con = abrir_conexao()
    con.execute(query, (nome, preco))
    con.commit()
    con.close()


def selecionar_itens(preco):
    con = abrir_conexao()
    cursor = con.execute(
        f"SELECT * FROM {TABELA} WHERE preco = ?",
        (preco,))
    res = cursor.fetchall()
    con.close()

    return res
