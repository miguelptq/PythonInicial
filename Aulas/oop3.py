class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def __str__(self):
        return (f'Tiular: {self.titular}\n'
                f'Saldo: {self.saldo}\n'
                f'Limite: {self.limite}')

    def __iter__(self):
        return iter({"titular": self.titular, "saldo": self.saldo, "limite": self.limite})


conta_pessoal = ContaBancaria("Ricardo", 1250, 400)
for c in conta_pessoal:
    print(c)
print(conta_pessoal)
