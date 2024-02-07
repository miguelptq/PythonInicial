def mensagem(msg):
    message = f"   {msg}   "
    total_width = int(len(message) / 2)
    print("-=" * total_width)
    print(message)
    print("-=" * total_width)
    print()


def validar(val):
    """
    -> Esta função serve para verificar se o valor é inteiro ou não
    :param val: valor a ser verificado
    :return: True caso seja numérico, False se não for
    """
    return True if val.isnumeric() else False


while True:
    valor = input("Digite um valor: ")
    if validar(valor):
        print(f'O valor "{valor}" é númerico')
        break
    else:
        print(f'O valor "{valor}" não é numérico!')

