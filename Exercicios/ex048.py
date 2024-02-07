numList = [[], []]
for i in range(0, 10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        numList[0].append(num)
    else:
        numList[1].append(num)
numList[0].sort()
numList[1].sort()
print(f"Números: {numList}")
print(f"Números Pares: {numList[0]}")
print(f"Números Impares: {numList[1]}")
