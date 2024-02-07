from random import randint
from time import sleep

optionsDict = {
            1: "Pedra",
            2: "Papel",
            3: "Tesoura"
        }
opcaoGerada = randint(1, 3)
print(optionsDict[opcaoGerada])

print("::: Escolha a opção :::")
print("[ 1 ] - Pedra")
print("[ 2 ] - Papel")
print("[ 3 ] - Tesoura")
userOption = int(input("Opção escolhida: "))
while userOption not in optionsDict.keys():
    print("Tente novamente uma opção valida")
    userOption = int(input("Opção escolhida: "))
print("Pedra...")
sleep(1)
print("Papel...")
sleep(1)
print("Tesoura...")
sleep(1)
print("\n---Analisando--\n\n")
sleep(2)

"""if userOption == opcaoGerada:
    print("Empate")
elif ((userOption == 3 and opcaoGerada == 1) or (userOption == 1 and opcaoGerada == 2) or
      (userOption == 2 and opcaoGerada == 3)):
    print(f"Perdeu!!  {optionsDict[opcaoGerada]} ganha a {optionsDict[userOption]}")
else:
    print(f"Ganhou!! {optionsDict[userOption]} ganha a {optionsDict[opcaoGerada]}")"""

if opcaoGerada - userOption == 0:
    print("Empate")
elif opcaoGerada - userOption in [-2,1]:
    print(f"Perdeu!!  {optionsDict[opcaoGerada]} ganha a {optionsDict[userOption]}")
else:
    print(f"Ganhou!! {optionsDict[userOption]} ganha a {optionsDict[opcaoGerada]}")
