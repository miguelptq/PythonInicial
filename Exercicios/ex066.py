from time import sleep


def mensagem(msg):
    message = f"   {msg}   "
    total_width = int(len(message) / 2)
    print("-=" * total_width)
    print(message)
    print("-=" * total_width)
    print()


def fatorial(num, mostrar):
    """
    -> Esta função retornará o fatorial de um número
    :param num: numero do qual irá ser calculado o fatorial
    :param mostrar: variavel que determinará se mostra a conta
    :return: no return
    """
    valor_final = 1
    for i in range(num, 0, -1):
        if mostrar:
            print(i, end=" x " if i != 1 else " = ")
            sleep(0.1)
        valor_final = valor_final * i
    return valor_final


mensagem("Calculador fatorial")
numero = int(input("Digite um número: "))
opcao = input("Deseja mostrar a conta do fatorial? [S/N]").lower().strip()
mostra = True if opcao == "s" else False
print(fatorial(numero, mostra))
