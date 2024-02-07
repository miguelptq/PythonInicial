aluno = dict()
aluno["nome"] = input("Nome do aluno: ")
aluno["media"] = float(input(f"Média de {aluno['nome']}: "))
if aluno["media"] >= 9.5:
    aluno["situacao"] = "Aprovado"
else:
    aluno["situacao"] = "Reprovado"

print(f"O aluno {aluno['nome']} como média {aluno['media']} encontra-se {aluno['situacao']}")