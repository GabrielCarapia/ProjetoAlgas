import mysql.connector

def criar_conexao(host, usuario, senha, banco, porta):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco, port=porta)


def fechar_conexao(con):
    return con.close()
