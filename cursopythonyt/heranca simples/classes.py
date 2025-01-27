
# A herança é um mecanismo que permite criar novas classes (subclasses ou classes filhas)
# a partir de classes existentes (superclasses ou classes pai).
# A classe filha herda todos os atributos e métodos da classe pai,
# podendo adicionar seus próprios atributos e métodos ou sobrescrever os métodos herdados.

# SUPER CLASSE - classe pai
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atribui o nome à instância da classe.
        self.idade = idade  # Atribui a idade à instância da classe.
        self.nomeclasse = self.__class__.__name__  # Armazena o nome da classe da instância.

    def falar(self):
        print(f"{self.nomeclasse} Falando...")  # Imprime uma mensagem indicando que a pessoa está falando.

# sub classe - classe filha
class Cliente(Pessoa):  # A classe Cliente herda da classe Pessoa.
    def comprar(self):
        print(f"{self.nomeclasse} comprando...")  # Método específico da classe Cliente.

class Aluno(Pessoa):  # A classe Aluno também herda da classe Pessoa.
    def estudar(self):
        print(f"{self.nomeclasse} estudando...")  # Método específico da classe Aluno.