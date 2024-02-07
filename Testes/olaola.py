class Conta:
    def __init__(self, nib, titular, saldo, limite):
        print("A contruir objeto...")
        self.nib = nib
        self.titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, valor):
        self.__limite = valor