num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))
num4 = int(input("Número 4: "))

tuple = (num1, num2, num3, num4)
pares = ""
numberFive = False
countNumberSeven = 0

for t in tuple:
    if t == 7:
        countNumberSeven += 1
    if t % 2 == 0:
        pares += str(t) + "~"

if countNumberSeven == 0 and 5 not in tuple and not numberFive:
    print("Não foram encontrados dados")
else:
    print(f"O número 7 foi encontrado: {countNumberSeven} vezes")
    if 5 in tuple:
        numberFive = True
        print("O número 5 encontra-se na posição",tuple.index(5))
    if not numberFive:
        print("O número 5 não foi encontrado")

    print(f"Números pares: {pares}FIM")

