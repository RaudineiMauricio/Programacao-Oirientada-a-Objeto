# Getters: Usados para obter o valor de um atributo.
# Setters: Usados para modificar o valor de um atributo.
# @property: Decorador que transforma um método em um getter ou setter.
# Vantagens: Encapsulamento, validação, formatação, cálculos.

# Por que usar getters e setters?

# Encapsulamento: Escondem a implementação interna dos atributos, tornando o código mais modular e fácil de manter.
# Validação: Permitem adicionar lógica para validar os valores atribuídos aos atributos, garantindo a integridade dos dados.
# Formatação: Podem formatar os valores antes de retorná-los, por exemplo, convertendo para maiúsculas ou formatando números.
# Cálculos: Podem realizar cálculos complexos ao acessar ou modificar um atributo.

# Quando usar getters e setters?

# Quando você precisa validar os dados antes de atribuí-los a um atributo.
# Quando você precisa realizar cálculos complexos ao acessar ou modificar um atributo.
# Quando você deseja controlar o acesso a um atributo.

# O uso de getters e setters torna seu código mais robusto e seguro,
# pois você tem controle sobre como os atributos são acessados e modificados.


class Produto:
    # Define uma classe chamada 'Produto' que serve como um modelo para criar objetos que representam produtos.
    def __init__(self, nome, preco):
        # Construtor da classe. Inicializa os atributos 'nome' e 'preco' de cada objeto criado.
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        # Calcula e aplica um desconto ao preço do produto.
        novo_preco = self.preco - (self.preco * (percentual / 100))
        # Utiliza o setter para garantir que todas as validações e conversões sejam aplicadas ao novo preço.
        self.preco = novo_preco

    # Getter para o atributo 'nome'. Permite acessar o valor do nome de forma controlada.
    @property
    def nome(self):
        return self._nome

    # Setter para o atributo 'nome'. Permite atribuir um novo valor ao nome,
    #  convertendo para maiúsculas no início de cada palavra.
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # Getter para o atributo 'preco'. Permite acessar o valor do preço de forma controlada.
    @property
    def preco(self):
        return self._preco

    # Setter para o atributo 'preco'. Permite atribuir um novo valor ao preço,
    #  convertendo strings para float se necessário.
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            # Remove o símbolo "R$" e converte para float.
            valor = float(valor.replace("R$", ""))
        self._preco = valor

# Cria um objeto 'Produto' chamado 'p1' com nome "CAMISA" e preço 50.
p1 = Produto("CAMISA", 50)
# Aplica um desconto de 10% ao produto p1.
p1.desconto(10)
# Imprime o nome e o preço atualizados do produto p1.
print(p1.nome, p1.preco)

# Cria um objeto 'Produto' chamado 'p2' com nome "CANECA" e preço "R$15".
p2 = Produto("CANECA", "R$15")
# Aplica um desconto de 10% ao produto p2.
p2.desconto(10)
# Imprime o nome e o preço atualizados do produto p2.
print(p2.nome, p2.preco)
