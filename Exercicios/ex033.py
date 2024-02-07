resultado = 0
count = 0
while True:
    valor = int(input("Valor: "))
    resultado += valor
    count += 1
    continuar = input("Quer continuar?[s/n]")
    if continuar == "n":
        break

print(f"Resultado: {resultado}, contagem: {count}")
