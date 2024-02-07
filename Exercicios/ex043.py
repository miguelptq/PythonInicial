lista = list()
for i in range(0, 5):
    num = int(input("Digite um úmero: "))
    lista.append(num)

maxValue = max(lista)
minValue = min(lista)

print(f"O valor mais alto é {maxValue} e encontra-se na posição {lista.index(maxValue)}")
print(f"O valor mais baixo é {minValue} e encontra-se na posição {lista.index(minValue)}")
