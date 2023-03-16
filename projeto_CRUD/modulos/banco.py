import sqlite3
from contextlib import closing


def criar(nome, * parametros):
    lista = []
    with sqlite3.connect("../banco.db") as conexao:
        with closing(conexao.cursor()) as cursor:
            for c in parametros:
                dados = {}
                tipo = input(f"Digite o tipo do parametro {c} - [text, integer]: ").lower()
                while tipo != "text" and tipo != "integer":
                    tipo = input(f"Digite o tipo do parametro {c} - [text, integer]: ").lower()
                dados["nome"] = c
                dados["tipo"] = tipo
                lista.append(dados.copy())
                dados.clear()
            for c in range(0, len(lista)):
                cursor.execute(f"create table {nome} ({lista[c]['nome']} {lista[c]['tipo']})")


criar("Cadastro_horas", "hora_entrada", "hora_saida", "relatorio")
