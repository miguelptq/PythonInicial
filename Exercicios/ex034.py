count = 0
maior = 0
menor = 0
soma = 0
valor = 0
while True:
    tempValue = valor
    valor = int(input("Nota: "))
    count += 1
    soma = soma + valor
    if valor >= tempValue:
        maior = valor
    if valor <= tempValue:
        menor = valor
    continuar = input("Quer continuar? ")
    if continuar == "n":
        break
media = soma / count
print(f"Contagem: {count}")
print(f"Media: {media}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")

