#importando da classse ContaCorrente

#conta é uma referência

from conta import Conta

'''conta = Conta()

#exibindo sem criar a variável na função
print("Essas exibições não contém a variável na função")
#self.numero = 548
        #self.titular = "Marcola"
        #self.saldo = 2540
        #self.limite = 2000

print(conta.numero, conta.titular, conta.saldo)

print('\n')'''

print("Essas exibições contém a variável na função e tenho que definir os paramêtros")
conta = Conta(20, "Marcus" , 500.54, 3000.00)
conta2 = Conta(1, "Marley", 1000.00, 200000.00)

print(f'Saldo conta 2: {conta2.saldo}')
print(f'Esse é o saldo da conta 1: {conta.saldo}')

print('**********************')

conta2.extrato()

#depositando na conta do Marley
conta2.depositar(200)
#conferindo valor
conta2.extrato()
#sacando na conta do Marley
conta2.sacar(520)
#conferindo valor
conta2.extrato()