def conversao(temp):
    print(f"A temperatura {temp} em Celsius é igual a {(temp * 9/5) + 32} em Fahrenheit")


def mensagem(msg):
    message = f"   {msg}   "
    total_width = int(len(message) / 2)
    print("-=" * total_width)
    print(message)
    print("-=" * total_width)
    print()


mensagem("Conversor de Celsius para Fahrenheit.")
temperatura = float(input("Digite uma temperatura em Celsius: "))
conversao(temperatura)
