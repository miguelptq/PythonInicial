# Importar randit para gerar um numero aleatorio

from random import randint
from time import sleep

print("Gerando um numero...")
sleep(3)
# Gerar um numero aleatorio entre 1 intervalo de numeros
randomNumber = randint(0, 7)
print(f"Random Number: {randomNumber}")
userNumber = int(input("Número escolhido pelo utilizador [0-7]: "))

print("A verificar...")
sleep(1)
# Verificar se o numero gerado e o numero do utilizador sao iguais
if userNumber > 7 or userNumber < 0:
    print("Escolha um numero entre 0 e 7")
elif userNumber == randomNumber:
    print(f"Ganhou!! O numero gerado foi {randomNumber} e escolheu {userNumber}")
else:
    print(f"Perdeu!! O numero gerado foi {randomNumber} e escolheu {userNumber}")