""""
public, protected, privvate - 
_ privado/protected (public)
__privado(_NOMECLASSE__nomeatributo)
"""

# Por que usar Encapsulamento?
# Proteção de Dados: Evita que os dados internos da classe
# sejam modificados de forma acidental ou intencional, garantindo a integridade dos objetos.
# Modularidade: Permite que você altere a implementação interna
# da classe sem afetar o código que a utiliza, desde que a interface pública (métodos) permaneça a mesma.
# Reutilização: Facilita a criação de classes mais robustas e reutilizáveis,
# pois você pode confiar que os dados internos da classe estão protegidos.
# Manutenção: Torna o código mais fácil de entender e manter,
# pois a lógica da classe está encapsulada e bem definida.
class Base_de_Dados:
    def __init__(self):
        self.__dados = {}  # Dicionário para armazenar os dados dos clientes.
                          # O duplo underline indica que é um atributo privado.

    #MÉTODOS PUBLICOS, PODEM SER CHAMADOS DE FORA DA CLASSE PARA INTERAGIR COM OS DADOS.	
    def inserir_cliente(self, id, nome):
        # Verifica se a chave "clientes" já existe no dicionário.
        if "clientes" not in self.__dados:
            self.__dados["clientes"] = {id: nome}  # Cria um novo dicionário para os clientes.
        else:
            self.__dados["clientes"].update({id: nome})  # Adiciona ou atualiza o cliente existente.

    def lista_clientes(self):
        for id, nome in self.__dados["clientes"].items():
            print(id, nome)  # Imprime os dados de cada cliente.

    def apaga_cliente(self, id):
        del self.__dados["clientes"][id]  # Remove o cliente com o ID especificado.

bd = Base_de_Dados()  # Cria uma instância da classe Base_de_Dados.
bd.inserir_cliente(1, "RAUL")
bd.inserir_cliente(2, "Gabi")
bd.__dados = "Outra coisa"  # Tentativa (inválida) de modificar diretamente o atributo privado.
print(bd.__dados)
print(bd._Base_de_Dados__dados)
# Ao tentar modificar diretamente o atributo __dados com bd.__dados = "Outra coisa",
#  Python renomeia o atributo para _Base_de_Dados__dados para evitar o acesso direto.
#  Essa é uma forma de "maquiar" o nome do atributo e dificultar a sua modificação.
# No entanto, é possível acessar o atributo privado usando o nome "maquiado" _Base_de_Dados__dados,
#  mas essa prática não é recomendada, pois viola o encapsulamento.