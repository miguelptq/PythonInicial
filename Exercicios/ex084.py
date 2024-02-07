class Temperatura:
    def __init__(self):
        self._valor = 0

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        self._valor = novo_valor

    def converter(self, tipo):
        if tipo == 'Fahrenheit':
            return (self._valor * 1.8) + 32
        elif tipo == 'Kelvin':
            return self._valor + 273.15
        else:
            print(f"{tipo} não é um tipo de temperatura")


temperatura = Temperatura()
temperatura.valor = float(input("Temperatura em Celsius: "))
tipo = input(f"Pretende converter {temperatura.valor} Celsius para que tipo?")
print(f"{temperatura.valor} Celsius = {temperatura.converter(tipo)} {tipo}")
