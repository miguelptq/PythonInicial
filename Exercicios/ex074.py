class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def imprimir_livro(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")


count = 1
livros = []
while count <= 3:
    livro = Livro(input("Nome do Livro: "), input("Nome do autor: "))
    livros.append(livro)
    count += 1
print("=== Lista de Livros ===")
for li in livros:
    li.imprimir_livro()
