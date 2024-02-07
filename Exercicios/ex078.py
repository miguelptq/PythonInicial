class Circulo:
    def __init__(self, raio):
        self.__raio = raio
        self.__pi = 3.14159265

    def set_raio(self, valor):
        print(f'O valor do raio foi modificado para {valor}!')
        self.__raio = valor

    def get_raio(self):
        return self.__raio

    def calcular_area(self):
        raio = self.__raio
        pi = self.__pi
        return pi * (raio * raio)

    def calcular_perimetro(self):
        raio = self.__raio
        pi = self.__pi
        return 2 * pi * raio


circulo = Circulo(5)
print(f"Raio:{circulo.get_raio()}")
print(f"Area: {circulo.calcular_area()}")
print(f"Perimetro: {circulo.calcular_perimetro()}")

Novo_Raio = int(input("Insira o novo raio do cirulo: "))
circulo.set_raio(Novo_Raio)
print(f"Raio:{circulo.get_raio()}")
print(f"Area: {circulo.calcular_area()}")
print(f"Perimetro: {circulo.calcular_perimetro()}")

