from classes import *  #NAO É RECOMENDADO IMPORTAR DESSE JEITO, MELHOR IMPORTAR O QUE FOR USAR.
"""
Associação - USA | Agregação - TEM | COMPOSIÇÃO - É DONO | Herença - É
"""
c1 = Cliente("Luiz", 45)
c1.falar()
c1.comprar()

a1 = Aluno ("Aline", 54)
a1.falar()
a1.estudar()

p1 = Pessoa("Messi", 34)
p1.falar()

#Vantagens da Herança:

# Reutilização de código: Evita a duplicação de código, pois as subclasses podem
#  reutilizar os métodos e atributos da superclasse.
# Hierarquia de classes: Permite criar uma hierarquia de classes,
#  organizando o código de forma mais clara e hierárquica.
# Polimorfismo: Permite que objetos de diferentes classes sejam tratados
#  de forma genérica, através de um método comum herdado da superclasse.