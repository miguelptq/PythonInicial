def area(largura, altura):
    a = round(larg * altura)
    print(f"Área: {a} m2")


def mensagem(msg):
    message = f"   {msg}   "
    total_width = int(len(message)/3)
    print("=-=" * total_width)
    print(message)
    print("=-=" * total_width)


mensagem("Calculador de área")
larg = float(input("Largura do seu terreno: "))
comprimento = float(input("Altura do seu terreno: "))

area(larg, comprimento)
