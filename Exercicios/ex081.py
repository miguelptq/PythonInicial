class Livro:
    def __init__(self):
        self.__titulo = ""
        self.__ano = 0
        self.__autor = ""
        self.__disponibildade = False

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def disponibildade(self):
        if disponibilidade_livro:
            return "O livro encontra-se disponivel!"
        else:
            return "O livro não se encontra disponivel!"

    @disponibildade.setter
    def disponibildade(self, disponibildade):
        self.__disponibildade = disponibildade


print("--- BIBLIOTECA ---")
input("Clique para adicionar um novo livro...")
nome_livro = input("Titulo do Livro: ")
ano_livro = int(input("Ano do Livro: "))
autor_livro = input("Autor do Livro: ")
disponibilidade_livro = input("Disponibilidade do Livro: ").strip().lower()
if disponibilidade_livro == "s":
    disponibilidade_livro = True
else:
    disponibilidade_livro = False

novo_livro = Livro()
novo_livro.titulo = nome_livro
novo_livro.ano = ano_livro
novo_livro.autor = autor_livro
novo_livro.disponibildade = disponibilidade_livro


print(novo_livro.titulo)
print(novo_livro.ano)
print(novo_livro.autor)
print(novo_livro.disponibildade)

input("Clique para alterar o livro...")
nome_livro = input("Titulo do Livro: ")
ano_livro = int(input("Ano do Livro: "))
autor_livro = input("Autor do Livro: ")
disponibilidade_livro = input("Disponibilidade do Livro: ").strip().lower()
if disponibilidade_livro == "s":
    disponibilidade_livro = True
else:
    disponibilidade_livro = False

novo_livro.titulo = nome_livro
novo_livro.ano = ano_livro
novo_livro.autor = autor_livro
novo_livro.disponibildade = disponibilidade_livro
print(novo_livro.titulo)
print(novo_livro.ano)
print(novo_livro.autor)
print(novo_livro.disponibildade)
