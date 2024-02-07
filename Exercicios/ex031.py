num = int(input("Indique um número para calcular o faturial: "))
resultado = 1
for i in range(num, 0, -1):
    resultado *= i

print(f"O fatorial de {num} é: {resultado}")