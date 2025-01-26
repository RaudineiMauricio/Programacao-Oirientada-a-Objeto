from random import randint
# Escolhendo o método certo:

#Pergunte-se: A operação precisa de informações específicas de uma instância? Se sim, use um método de instância.
#Pergunte-se: A operação está relacionada à classe como um todo, ou poderia existir fora dela? Se sim, considere um método estático.
#Pergunte-se: A operação precisa criar uma nova instância da classe de forma diferente do construtor padrão? Se sim, use um método de classe.
# Ao entender essas diferenças, você poderá escrever código Python mais organizado, eficiente e fácil de manter.


class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    #metodo de instância - precisa de uma instância para ser usado.
    #PRECISA O PARÂMETRO SELF
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)


    #Metodo de classe Operam sobre a classe: Acionam funcionalidades relacionadas à classe como um todo,
    # não a uma instância específica.
    #Quando usar:
    #Criar métodos de fábrica: Criar instâncias de uma classe de forma alternativa,
    #com base em diferentes tipos de dados.
    #Acessar atributos de classe: Modificar ou acessar atributos que pertencem à classe,
    #não a instâncias individuais.
    #Operações que não dependem de um estado específico:
    # Por exemplo, um método from_string que cria uma instância de uma classe a partir de uma string.
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    

    #Métodos Estáticos
    #Não estão ligados a instâncias ou classes: São funções regulares dentro de uma classe, mas não têm acesso a self ou cls.
    #Quando usar:
    #Funções utilitárias: Funções que não dependem de nenhum estado da classe ou instância.
    #Métodos que poderiam existir fora da classe: Mas são colocados na classe por razões de organização ou #namespace.
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

#p1 = Pessoa.por_ano_nascimento("Luiz", 1987)

p1 = Pessoa("Luiz", 32)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
print(p1.gera_id())