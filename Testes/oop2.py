class Conta:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.__saldo = saldo
        self.limite = limite

    @property
    def saldo(self):
        return f'O saldo da conta é  {self.__saldo}€'

    @saldo.setter
    def saldo(self, valor):
        if valor > 1000:
            print(f'O valor {valor} € é superior ao limite permitido')
        else:
            self.__saldo = valor
            print('O saldo foi alterado com sucesso')


conta = Conta("Miguel", 1250, 300)
print(conta.saldo)
conta.saldo = 1500
print(conta.saldo)

