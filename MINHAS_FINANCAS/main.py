#APRENDENDO SOBRE CLASSES

from utilitarios import (
    cadastrar_categoria,
    cadastrar_transacao,
    saldo_total,
)

#CATEGORIAS
categoria_receitas = cadastrar_categoria("RECEITAS")
categoria_contas = cadastrar_categoria("CONTAS FIXAS")
categoria_lazer = cadastrar_categoria("LAZER")
categoria_viagens = cadastrar_categoria("VIAGENS")

#TRANSAÇÕES
cadastrar_transacao(
    descricao = "Salário jan/2024", valor=1000.0, categoria=categoria_receitas
)


cadastrar_transacao(descricao="Mesada Mamãe", valor=50.0, categoria=categoria_receitas)

cadastrar_transacao(descricao="Ingresso Show", valor=-150.0, categoria=categoria_lazer)

cadastrar_transacao(descricao="Conta de Luz", valor=-100.00, categoria=categoria_contas)

cadastrar_transacao(descricao="Disney", valor=-400.00, categoria=categoria_viagens)

total = saldo_total()

print("O saldo total: ",total)

print(f"-=" * 30)
