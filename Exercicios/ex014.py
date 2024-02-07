LIMITE_VELOCIDADE = 80
VALOR_INICIAL_MULTA = 100
MULTA_MULTIPLAYER = 7

velocidade = int(input("Velocidade: "))

if velocidade > LIMITE_VELOCIDADE:
    multa = (velocidade - LIMITE_VELOCIDADE) * MULTA_MULTIPLAYER + VALOR_INICIAL_MULTA
    print(f"Multa: {multa}€")
else:
    print("Não multado!")