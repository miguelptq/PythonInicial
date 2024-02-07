#Crie um programa que leia vários números e coloca-os numa lista.
# Crie duas listas adicionais que vão conter os números pares e impares da lista principal.
# No final mostre todas as listas.

numeros = list()
pares = list()
impares = list()
while True:
    num = int(input("Digite um número: "))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    option = input("Deseja continuar? [S/N]")
    if option.lower() == "n":
        break
print(f"Lista de números: {numeros}")
print(f"Lista de número pares: {pares}")
print(f"Lista de número imares:  {impares}")
