def calcular_dados_aluno(a):
    soma_notas = 0
    for v in a["notas"]:
        soma_notas += v
    media_aluno = soma_notas / len(a["notas"])
    msg = f"O aluno {a["nome"]} tem a média de {media_aluno} logo está "
    if media_aluno >= 9.5:
        situacao = "Aprovado!"
    else:
        situacao = "Reprovado!"
    print(msg + situacao)


aluno = dict()
aluno["nome"] = input("Digite o nome do aluno: ")
notas = list()
while True:
    nota = float(input(f"Nota do aluno {aluno["nome"]}: "))
    notas.append(nota)
    opcao = input("Deseja continuar? [s/n]").lower().strip()
    if opcao == "n":
        break
aluno["notas"] = notas
calcular_dados_aluno(aluno)
