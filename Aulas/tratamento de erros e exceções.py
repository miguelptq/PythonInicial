def divisao(a, b):
    div = a / b
    return div


try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo numero: "))
    var = divisao(10, 0)

except ZeroDivisionError:
    print("ERRO! A DIVISÃO POR ZERO NÃO É POSSIVEL")
except ValueError:
    print("O utilizador não digitou números inteiros")
except KeyboardInterrupt:
    print("Programa foi fechado inesperadamente!!")
else:
    print("A divisão é possivel")

finally:
    print("TERMINOU")
