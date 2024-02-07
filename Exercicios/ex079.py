class ContaBancaria:
    def __init__(self):
        print(f"Conta criado com sucesso!")
        self.__nib = "Nib"
        self.__titular = "Titular"
        self.__saldo = 0
        self.__limite = 0

    def set_nib(self, nib):
        self.__nib = nib

    def get_nib(self):
        return  self.__nib

    def set_titular(self, titular):
        self.__titular = titular

    def get_titular(self):
        return self.__titular

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def set_limite(self, limite):
        self.__limite = limite

    def get_limite(self):
        return self.__limite


Nib_Titular = int(input("Nib do Titular: "))
Nome_Titular = input("Nome do Titular: ")
Saldo_Titular = int(input("Saldo do Titular: "))
Limite_Titular = int(input("Limite do Titular: "))

conta = ContaBancaria()
conta.set_nib(Nib_Titular)
conta.set_titular(Nome_Titular)
conta.set_saldo(Saldo_Titular)
conta.set_limite(Limite_Titular)


print(f"Nib do Titular: {conta.get_nib()}")
print(f"Nome do Titular: {conta.get_titular()}")
print(f"Saldo do Titular: {conta.get_saldo()}€")
print(f"Limite do Titular: {conta.get_limite()}€")