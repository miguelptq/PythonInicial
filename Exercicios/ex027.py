menorIdade = 0
maiorIdade = 0

for i in range(0, 10):
    idade = int(input("Idade: "))
    if maiorIdade < idade:
        maiorIdade = idade
    if menorIdade == 0 or idade < menorIdade:
        menorIdade = idade

print(f"Maior Idade: {maiorIdade}")
print(f"Menor Idade: {menorIdade}")