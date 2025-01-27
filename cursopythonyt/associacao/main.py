from classes import Escritor
from classes import Caneta
from classes import Maquina_Escrever

#
escritor = Escritor("RAUL")
caneta = Caneta("Bic")
maquina = Maquina_Escrever()

#fazendo assosiacão entre um escritor e uma máquina de escerver.
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

