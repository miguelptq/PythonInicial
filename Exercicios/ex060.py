from time import sleep


def contagem(inicio, fim, passos):
    if passos < 0:
        passos *= -1
    if passos == 0:
        passos = 1
    print(f"Contagem de {inicio} até {fim} de {passos} em {passos}")
    if inicio < fim:
        for i in range(inicio, fim, passos):
            print(i, end=" ", flush=True)
            sleep(0.2)
    else:
        for i in range(inicio, fim - 1, -passos):
            print(i, end=" ", flush=True)
            sleep(0.2)
    print()


def mensagem(msg):
    message = f"   {msg}   "
    total_width = int(len(message) / 2)
    print("-=" * total_width)
    print(message)
    print("-=" * total_width)
    print()


contagem(1, 20, 2)
contagem(10, 0, 1)
print()
mensagem("Contagem Personalizada")
start = int(input("Início da Contagem: "))
end = int(input("Fim da Contagem: "))
steps = int(input("Passos da Contagem: "))
contagem(start, end, steps)
