def divisao (n1, n2):
    return  n1 / n2


conta = None
while conta is None:
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        conta = divisao(num1, num2)
        print(f"A divisão de {num1} por {num2} é {conta}")
    except ZeroDivisionError:
        print("Não é possível dividir por 0")
    except ValueError:
        print("O número introduzido não é valido")

