def insere_linha():
    print("=-=-=-=-=-=-=")


def mensagem(msg, total_width):
    dashes_on_each_side = (total_width - len(msg)) // 2
    print("=" * total_width)
    # Create the centered message with dashes
    centered_message = "=" * dashes_on_each_side + msg + "=" * dashes_on_each_side
    # Print the centered message
    print(centered_message)
    print("=" * total_width)


def soma(a, b):
    s = a + b
    print(f"A soma entre {a} e {b} é igual a {s}")


def conta_numeros(*num):
    print(len(num))
    print()
    for numeros in num:
        print(f"{numeros}", end=" ")


msg = "Mundo das Funções"
mensagem(msg, len(msg))

soma(2, 5)
soma(3, 16)
soma(4, 4)

print()
msg = "Função Desempacutar"
mensagem(msg, len(msg))
conta_numeros(1, 2, 3, 4, 5, 6)
conta_numeros(1, 3, 5)
conta_numeros(1, 10, 12, 14, 17)
