frase = input("Escreva uma frase:").upper().strip()

print("A letra 'A' aparece {} vezes.".format(frase.count("A")))
print("O primeiro 'A' está na posição: {}.".format(frase.find("A") + 1))
print("O ultimo 'A' está na posição: {}.".format(frase.rfind("A") + 1))