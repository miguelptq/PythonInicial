from ex072Modulo import calculadora, tabuada, par_impar, numero_primo, fatorial


def menu():
    opcao = None
    while True:
        print("=" * 30)
        print("[1] Calculdora")
        print("[2] Tabuada")
        print("[3] Par ou Ímpar")
        print("[4] Números Primos")
        print("[5] Factorial")
        print("=" * 30)
        try:
            opcao = int(input("Escolha uma opção ->"))
        except ValueError:
            print("A opção tem de ser um valor inteiro")
        if opcao == 1:
            calculadora()
        elif opcao == 2:
            tabuada()
        elif opcao == 3:
            par_impar()
        elif opcao == 4:
            numero_primo()
        elif opcao == 5:
            fatorial()


menu()
