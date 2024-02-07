def helper(c):
    """c_data = c.__doc__"""
    help(c)


def mensagem(msg):
    message = f"   {msg}   "
    total_width = int(len(message) / 2)
    print("-=" * total_width)
    print(message)
    print("-=" * total_width)
    print()


mensagem("Interactive Helper")
while True:
    comando = input("Comando a pesquisar: ")
    if comando.upper() == "FIM":
        break
    else:
        helper(comando)
    #print(comando_data)
