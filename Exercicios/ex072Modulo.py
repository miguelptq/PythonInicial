from time import sleep


def soma(n1, n2):
    return n1 + n2


def multiplicao(n1, n2):
    return n1 * n2


def divisao(n1, n2):
    return n1 / n2


def subtracao(n1, n2):
    return n1 - n2


def calculadora():
    resultado = None
    while resultado is None:
        try:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o seundo número: "))
            sinal = input("Digite o sinal da conta [+, x, /, -]: ")
            while sinal not in "/x+-":
                print("Sinal inválido!!")
                sinal = input("Digite o sinal da conta [+, x, /, -]: ")
            if sinal == "+":
                resultado = soma(num1, num2)
            elif sinal == "x":
                resultado = multiplicao(num1, num2)
            elif sinal == "/":
                resultado = divisao(num1, num2)
            elif sinal == "-":
                resultado = subtracao(num1, num2)
        except ValueError:
            print("O número introduzido não é valido")
        except ZeroDivisionError:
            print("Não é possível dividir por 0")
        else:
            print(f"{num1} {sinal} {num2} = {resultado}")


def tabuada():
    try:
        num = int(input("Digite um número para calcular a tabuada: "))
        for i in range(1, 11):
            conta = i * num
            print(f"{num} x {i} = {conta}")
    except ValueError:
        print("O número introduzido não é valido")


def par_impar():
    try:
        num = int(input("Digite um número para saver se é par ou impar: "))
        if num % 2 == 0:
            print(f"O número {num} é par!")
        else:
            print(f"O número {num} é impar!")
    except ValueError:
        print("O número introduzido não é valido")


def numero_primo():
    try:
        count = 0
        num = int(input("Digite um número para saver se é primo: "))
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count <= 2:
            print(f"O numero {num} é primo")
        else:
            print(f"O número {num} não é primo")
    except ValueError:
        print("O número introduzido tem de ser inteiro")


def fatorial():
    """
    -> Esta função retornará o fatorial de um número
    :return: no return
    """
    num = int(input("Digite um número: "))
    valor_final = 1
    for i in range(num, 0, -1):
        print(i, end=" x " if i != 1 else " = ")
        sleep(0.1)
        valor_final = valor_final * i
    print(valor_final)

