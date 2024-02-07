import random


class Jogo:
    def __init__(self):
        self._jogada_gerada = ""
        self._jogada = ""

    @property
    def jogada_gerada(self):
        return self._jogada_gerada

    @jogada_gerada.setter
    def jogada_gerada(self, nova_jogada_gerada):
        self._jogada_gerada = nova_jogada_gerada

    @property
    def jogada(self):
        return self._jogada

    @jogada.setter
    def jogada(self, nova_jogada):
        self._jogada = nova_jogada

    def jogar(self):
        if self.jogada == self.jogada_gerada:
            print("Empatade!!")
        elif self.jogada == 1 and self.jogada_gerada == 2 or self.jogada == 2 and self.jogada_gerada == 1:
            print("Papel ganha a Pedra!!")
        elif self.jogada == 2 and self.jogada_gerada == 3 or self.jogada == 3 and self.jogada_gerada == 2:
            print("Tesoura ganhada a Papel!!")
        else:
            print("Pedra ganha a Tesoura!!")


jogo = Jogo()
jogo.jogada_gerada = random.randint(1, 3)
jogo.jogada = int(input("[1] Pedra\n"
                        "[2] Papel\n"
                        "[3] Tesoura\n"
                        "Escolha uma Opçao: "))
jogo.jogar()
