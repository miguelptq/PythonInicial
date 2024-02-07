class Jogo:
    def __init__(self, titulo, consola, preco):
        self.titulo = titulo
        self.consola = consola
        self.preco = preco


jogo = Jogo("Palworld", "PC", 29.90)

print(jogo.titulo)
print(jogo.consola)
print(jogo.preco)
