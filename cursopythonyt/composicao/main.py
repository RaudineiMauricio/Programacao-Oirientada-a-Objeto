from classes import Cliente

cliente1 = Cliente("Raul", 29)
cliente1.inserir_endereco("Brasilia", "DF")
print(cliente1.nome)
cliente1.lista_enderecos()
print()

cliente2 = Cliente("Luiz", 32)
cliente2.inserir_endereco("Belo Horizonte", 32)
cliente2.inserir_endereco("Rio de Janeiro", "RJ")
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente("João", 19)
cliente3.inserir_endereco("São Paulo", "SP")
print(cliente3.nome)
cliente3.lista_enderecos()
print()



# A relação entre as classes Cliente e Endereco é um exemplo clássico de composição.
# Na composição, um objeto (no caso, o Cliente) é composto por outros objetos (os Endereco).
# Isso significa que:
# Vida útil: A vida útil de um objeto composto está ligada à vida útil de seus componentes.
# Se um objeto Cliente for destruído, todos os seus endereços também serão destruídos, 
# pois fazem parte dele.
# Sem existência independente: Um Endereco, nesse contexto, não faz sentido existir por si só,
# fora do contexto de um cliente. Ele sempre estará associado a um cliente.