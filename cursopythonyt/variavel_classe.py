# Variáveis de Classe: Pertencem à classe e são compartilhadas por todas as instâncias.
#  Modificar uma variável de classe afeta todas as instâncias.
# Instâncias: São objetos criados a partir de uma classe.
#  Cada instância possui seu próprio espaço de nomes.
# Método Construtor: É um método especial chamado quando uma nova instância é criada.
#  É usado para inicializar os atributos da instância.

class A:
    vc = 123

    def __init__(self):
        pass


a1 = A()
a2 = A()

A.vc = "Flamengo"

print(a1.vc)
print(a2.vc)
print(A.vc)