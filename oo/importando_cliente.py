from http import client
from cliente import Cliente

#imprimimndo sem método
cliente = Cliente("marcus")
print(cliente.nome)
cliente.get_nome()

#criando método para definir primeira letra maiscula
#cliente = Cliente("marley")
#cliente.get_nome()