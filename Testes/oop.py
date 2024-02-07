class Conta:
    def __init__(self, identidade, titular, saldo, limite):
        self.identidade = identidade
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"A conta {self.identidade} tem {self.saldo} € disponíveis!")

    def levantar(self, valor):
        if valor > self.limite:
            print(f"O seu limite é de {self.limite}€ diários")
        else:
            if self.saldo > valor:
                self.saldo -= valor
            else:
                print(f"Só consegue levantar {self.saldo - self.limite}")

    def depositar(self, valor):
        self.saldo += valor


conta = Conta(input("Idendidade: "), input("Titular"), int(input("Saldo: ")), int(input("Limite: ")))

