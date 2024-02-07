from random import randint
from time import sleep

numPalpites = int(input("Número de palpites: "))
print("A gerar chaves.", end="")
sleep(1)
print(".", end="")
sleep(1)
print(".")

# Correr o numero de palpites
for i in range(0, numPalpites):
    chave = [[0, 0, 0, 0, 0], [0, 0]]
    for j in range(0, len(chave[0])):
        while True:
            randomNumber = randint(1, 50)
            if randomNumber not in chave[0]:
                chave[0][j] = randomNumber
                break
    for c in range(0, len(chave[1])):
        while True:
            randomNumber = randint(1, 12)
            if randomNumber not in chave[1]:
                chave[1][c] = randomNumber
                break
    numbers = ", ".join(str(num) for num in chave[0])
    stars = ", ".join(str(num) for num in chave[1])
    print(f"{i + 1} º Chave gerada-> Números: {numbers} -> Estrelas Geradas: {stars}")
