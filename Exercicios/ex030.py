num1 = 0
num2 = 0
num3 = 0
opcao = 4
resultado = 0
while opcao != 5:
    if opcao == 4:
        num1 = int(input("Numero 1: "))
        num2 = int(input("Numero 2: "))
        num3 = int(input("Numero 3: "))
    print(" [ 1 ] SOMAR")
    print(" [ 2 ] MULTIPLICADOR")
    print(" [ 3 ] MAIOR")
    print(" [ 4 ] NOVOS NÚMEROS")
    print(" [ 5 ] SAIR DO PROGRAMA")
    opcao = int(input("Opcao: "))
    if opcao == 1:
        resultado = num1 + num2 + num3
    elif opcao == 2:
        resultado = num1 * num2 * num3
    elif opcao == 3:
        resultado = max(num1, num2, num3)
    if opcao not in [1, 2, 3, 4, 5]:
        print("Opcao invalida")
    elif opcao != 4 and opcao != 5:
        print(f"Resultado: {resultado}")
    elif opcao == 5:
        print("Programa terminado")

