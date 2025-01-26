from categoria import Categoria
from transacao import Transacao

LISTA_CATEGORIAS = []
LISTA_TRANSACOES = []

def cadastrar_categoria(nome):
    nova_categoria = Categoria(nome = nome)

    LISTA_CATEGORIAS.append(nova_categoria)

    return nova_categoria


def cadastrar_transacao(descricao, valor, categoria):
    nova_transancao = Transacao(
        descricao = descricao,
        valor=valor,
        categoria = categoria
    )
        
    LISTA_TRANSACOES.append(nova_transancao)

    return nova_transancao

def saldo_total():
    total = 0
    
    for t in LISTA_TRANSACOES:
        total += t.valor

    return total
