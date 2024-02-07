frase = input("Digite a sua frase: ").strip()
# Remover espaços em branco e alterar para lower case a frase inteira
lowerFrase = "".join(frase.split()).lower()

# Reverter a frase
reversedWord = ""
for i in range(len(lowerFrase) - 1, -1, -1):
    reversedWord = reversedWord + lowerFrase[i]

# Alternativa a reverted frase
# reversedWord = lowerFrase[::-1]
if reversedWord == lowerFrase:
    print(f"A frase {frase} é palíndromo")
else:
    print(f"A frase {frase} não é palíndromo")