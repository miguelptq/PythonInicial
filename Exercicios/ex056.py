pessoas = []
while True:
    pessoa = dict()
    pessoa['nome'] = input("Nome da Pessoa: ")
    pessoa['sexo'] = input(f"Género de {pessoa['nome']}: ")
    pessoa['idade'] = int(input(f"Idade de {pessoa['nome']}"))
    pessoas.append(pessoa)
    opcao = input("Deseja continuar? [s/n]")
    if opcao == 'n':
        break
totalPessoas = 0
somaIdades = 0
mulheres = 0
somaIdadesHomem = 0
homens = 0
homensList = []
homensCimaMedia = 0
for pessoa in pessoas:
    totalPessoas += 1
    somaIdades += pessoa['idade']
    if pessoa['sexo'] == 'f':
        mulheres += 1
    if pessoa['sexo'] == 'm':
        homens += 1
        somaIdadesHomem += pessoa['idade']
        homensList.append(pessoa)
mediaIdades = somaIdades / totalPessoas
mediaHomem = somaIdadesHomem / homens
for homen in homensList:
    if homen['idade'] > mediaHomem:
        homensCimaMedia += 1
print(f"Pessoas Registadas: {totalPessoas}")
print(f"Média de Idades: {round(mediaIdades, 2)}")
print(f"Mulheres Registadas: {mulheres}")
print(f"Homens com Idade Acima da Média: {homensCimaMedia}")
