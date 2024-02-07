from header import header
from matematica import calculadora


header("Calculadora Mágica")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
sinal = input("Qual operação deseja fazer  a operaçao [ + - * /]: ")

print(f"{num1} {sinal} {num2} = {calculadora(num1, num2, sinal)}")
