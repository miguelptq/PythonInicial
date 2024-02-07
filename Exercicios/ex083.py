class ContaBancaria:
    def __init__(self):
        self.__titular = ""
        self.__saldo = 0
        self.__limite = 0

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, titular):
        self.__titular = titular

    def depositar(self, quantiade):
        print(f"Foram depositados {quantiade}€ com sucesso")
        self.__saldo += quantiade

    def sacar(self, quantidade):
        if quantidade > self.limite:
            print(f"O seu limite diário é de {self.limite} € e está a tentar levantar {quantidade} €")
        else:
            if quantidade <= self.saldo:
                print(f"Foram levantados {quantidade}€ com sucesso")
                self.saldo -= quantidade
                return True
            else:
                print(f"Não pode levantar {quantidade} €, pois tem apenas {self.saldo} €")

    def extrato(self):
        print(f"Saldo disponível: {self.saldo}€")

    def ver_conta(self):
        print(f"Títular: {self.titular}, Saldo {self.saldo}, Limite {self.limite}")


print("=== Registar Cliente ===")
nome_tiular = input("Titular: ")
conta = ContaBancaria()
conta.titular = nome_tiular
conta.saldo = int(input("Saldo: "))
conta.limite = int(input("Limite: "))
print(f"{nome_tiular} foi registado com sucesso!")
print("="*30)
while True:
    print("[1] Ver Conta")
    print("[2] Depositar Dinheiro")
    print("[3] Leventar Dinheiro")
    print("[4] Ver Saldo")
    print("[5] Sair")
    opcao_menu = int(input("Opcão escolhida: "))
    if opcao_menu == 1:
        conta.ver_conta()
    elif opcao_menu == 2:
        conta.depositar(int(input("Pretende depositar quanto na conta? ")))
    elif opcao_menu == 3:
        while True:
            possivel_levantamento = conta.sacar(int(input("Quanto pretende levantar? ")))
            if possivel_levantamento is True:
                break
    elif opcao_menu == 4:
        conta.extrato()
    elif opcao_menu == 5:
        print("Programa terminado!!")
        break
    else:
        print("Escolha uma opcao entre 1 a 5")
