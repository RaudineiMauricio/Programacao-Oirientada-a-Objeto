from classes import Carrinho_de_Compras, Produto

#A associação entre Carrinho_de_Compras e Produto permite que um carrinho tenha muitos produtos.
# A classe Carrinho_de_Compras fornece métodos para adicionar, listar e calcular o valor total
# dos produtos no carrinho.
# A classe Produto representa um produto individual e armazena suas informações básicas.

carrinho = Carrinho_de_Compras()

p1 = Produto("Camiseta", 100)
p2 = Produto("iphone", 8000)
p3 = Produto("Caneca", 25)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()
print("O valor total da compra é: ", carrinho.soma_total())

