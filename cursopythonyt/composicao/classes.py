
# Modelagem mais precisa: A composição permite modelar relações "tem um" de forma mais precisa.
# Um cliente tem endereços, assim como um carro tem rodas.
# Reutilização de código: Ao criar classes menores e mais específicas (como Endereco),
# você pode reutilizá-las em diferentes partes do seu programa.
# Organização do código: A composição ajuda a organizar o código em classes
# menores e mais coesas, facilitando a manutenção e a compreensão.



class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome  # Atribui o nome do cliente ao objeto.
        self.idade = idade  # Atribui a idade do cliente ao objeto.
        self.enderecos = []  # Inicializa uma lista vazia para armazenar os endereços do cliente.

    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))  # Adiciona um novo endereço à lista de endereços do cliente.

    def lista_enderecos(self):  # Imprime todos os endereços do cliente.
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade  # Atribui a cidade ao endereço.
        self.estado = estado  # Atribui o estado ao endereço.