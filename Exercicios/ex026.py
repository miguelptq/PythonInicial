from datetime import date
# Get current year
currentYear = date.today().year

# Iniciar variaveis de controlo
contagemMaior = 0
contagemMenor = 0

for i in range(0, 7):
    anoNasc = int(input("Ano de Nascimento: "))
    idade = currentYear - anoNasc
    if idade >= 18:
        contagemMaior += 1
    else:
        contagemMenor += 1
print(f"Existem {contagemMaior} pessoas que são maiores de idade")
print(f"Existem {contagemMenor} pessoas que são menores de idade")