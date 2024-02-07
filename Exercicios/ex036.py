from random import randint
vitorias = 0
while True:
    randomNumber = randint(1, 10)
    num = int(input("Escolha um numero: "))
    print("[ 1 ] Par")
    print("[ 2 ] Impar")
    opcao = int(input("Opcão Escolhida: "))
    soma = randomNumber + num
    if soma % 2 == 0 and opcao == 1 or soma % 2 != 0 and opcao == 2:
        vitorias += 1
    else:
        print("Perdeu")
        break

print(f"Programa terminado com o total de {vitorias} vitórias")