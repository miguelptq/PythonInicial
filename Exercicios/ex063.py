from time import sleep


def tabuada(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")
        sleep(0.2)


number = int(input("Digite um número para calcular a tabuada: "))
tabuada(number)