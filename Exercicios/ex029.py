from random import randint
from time import sleep
print("--------------------------------------")
print("---- BEM VINDO AO JOGO D ADIVINHA ----")
input("_______ PRESS ENTER TO CONTINUE ______")
count = 0
print("Gerando um numero...")
sleep(1)
# Gerar um numero aleatorio entre 1 intervalo de numeros
randomNumber = randint(0, 10)
print(randomNumber)
print("Qual é a sua tentativa")
resp = int(input("-----> "))
if resp < randomNumber:
    print("Mais a cima")
else:
    print("Mais a baixo")
count += 1
while resp != randomNumber:
    print("Errou !!! Tente novamente")
    resp = int(input("-----> "))
    if resp < randomNumber:
        print("Mais a cima")
    else:
        print("Mais a baixo")
    count += 1
if count == 1:
    print("Parabéns, acertou à primeira")
else:
    print(f"\nParabéns, acertou passado {count} tentativa/s")