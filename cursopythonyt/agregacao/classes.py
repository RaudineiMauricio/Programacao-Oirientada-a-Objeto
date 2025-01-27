# Na programação orientada a objetos, a associação é um relacionamento entre classes que indica que objetos
# de uma classe "conhecem" ou "usam" objetos de outra classe. Em outras palavras,
# uma classe pode ter atributos que são instâncias de outras classes.


class Carrinho_de_Compras:
    def __init__(self):
        self.produtos = []  # Inicializa uma lista vazia para armazenar os produtos.

    def inserir_produto(self, produto):
        self.produtos.append(produto)  # Adiciona um produto à lista de produtos.

    def lista_produto(self):  # Imprime os produtos do carrinho.
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):  # Calcula o valor total dos produtos no carrinho.
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome  # Atributo para armazenar o nome do produto.
        self.valor = valor  # Atributo para armazenar o valor do produto.
