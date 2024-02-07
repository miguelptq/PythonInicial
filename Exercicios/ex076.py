class Produto:
    def __init__(self, nome, stock):
        self.nome = nome
        self.stock = stock

    def adicionar_stock(self, quantidade):
        self.stock += quantidade

    def mostrar_stock(self):
        print(f"O produto {self.nome} tem o stock de  {self.stock}")


produto = Produto(input("Nome do produto: "), int(input("Quantidade em stock: ")))
produto.mostrar_stock()
print("Adicionar 100 de stock!")
produto.adicionar_stock(100)
produto.mostrar_stock()
