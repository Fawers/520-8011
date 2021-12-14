import sqlite3

BANCO = 'mercado.db.sqlite3'

def abrir_conexao():
    return sqlite3.connect(BANCO)
