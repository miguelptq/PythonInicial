numList = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
soma = 0

for i in range(0, len(numList)):
    for j in range(0, len(numList[i])):
        valor = int(input(f"Digite um valor para [{i}][{j}]: "))
        numList[i][j] = valor
        if valor % 2 == 0:
            pares += valor
        if j == 1:
            soma += valor
for i in range(0, len(numList)):
    for j in range(0, len(numList[i])):
        print(numList[i][j], end=" ")
    print("")
maxNum = max(numList[2])

print(f"Soma de todos os pares: {pares}")
print(f"Soma dos valores da segunda coluna: {soma}")
print(f"Maior valor da terceira linha: {maxNum}")
