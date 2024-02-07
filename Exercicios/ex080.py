class Aluno:
    def __init__(self):
        self.__nome_aluno = ""
        self.__notas = []

    def set_nome_aluno(self, nome):
        self.__nome_aluno = nome

    def get_nome_aluno(self):
        return self.__nome_aluno

    def set_notas(self, nota):
        self.__notas.append(nota)

    def get_notas(self):
        return self.__notas

    def calcular_media(self):
        notas = ', '.join([str(nota) for nota in self.__notas])
        print(f"O aluno {self.__nome_aluno} teve esta lista de notas: [{notas}]")
        soma_notas = 0
        for n in self.__notas:
            soma_notas += n
        count_notas = len(self.__notas)
        return soma_notas / count_notas


aluno = Aluno()
nome_aluno = input("Nome do Aluno:")
print("---  Notas do Aluno ---")
count = 1
while True:
    nota = float(input(f"Nota do Aluno no Exercicio {count}: "))
    aluno.set_notas(nota)
    count += 1
    opcao = input("Pretende adicionar mais notas [S/N]").lower().strip()
    if opcao == "n":
        break
print(f"Media do Aluno: {aluno.calcular_media()} valores")

