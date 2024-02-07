maisVinteCinco = 0
hMenosDezassete = 0
mulheres = 0
menorIdade = 0

while True:
    idade = int(input("Idade: "))
    sexo = input("Masculino ou Feminino[M/F]: ")
    if sexo == 'F':
        mulheres += 1
    if idade > 25:
        maisVinteCinco += 1
    elif idade < 18:
        menorIdade += 1
        if idade < 17 and sexo == 'M':
            hMenosDezassete += 1
    opcao = input("Deseja continuar? [S/N]")
    if opcao == 'N':
        break
print(f"Número de pessoas com mais de 25 anos: {maisVinteCinco}")
print(f"Número de homens com menos de 17: {hMenosDezassete}")
print(f"Número de mulheres registados: {mulheres}")
print(f"Número de menores de idade: {menorIdade}")