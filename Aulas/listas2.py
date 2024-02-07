turma = list()
aluno = list()

for c in range(0,3):
    aluno.append(input("Digite o nome do aluno: "))
    aluno.append(int(input("Digite a sua idade: ")))
    turma.append(aluno[:])
    aluno.clear()

for i, a in enumerate(turma):
    print(f"O {i+1} é o {a[0]} que tem {a[1]} anos")

for i in range(0, len(turma)):
    for aluno in range(0, len(turma[0])):
        print(f"{i + 1}")
        print(turma[i][aluno])
