class Produto:
    def __init__(self, nome):
        self.__nome = nome
        self.__stock = 0

    @property
    def nome(self):
        return f"Nome: {self.__nome}"

    @property
    def stock(self):
        stock = self.__stock
        if self.__stock < 0:
            stock = 0
        return f'Quantiade disponível: {stock}'

    @stock.setter
    def stock(self, valor):
        self.__stock = valor

    def adicionar_stock(self, valor):
        self.__stock += valor


produto = Produto("Batata")
produto.stock = 3
produto.adicionar_stock(1)
print(produto.nome)
print(produto.stock)
produto = Produto("Arroz")
produto.stock = -1
print(produto.nome)
print(produto.stock)
produto = Produto("Batata")
produto.stock = 3
print(produto.nome)
print(produto.stock)
