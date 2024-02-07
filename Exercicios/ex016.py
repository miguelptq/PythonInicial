# Ler numeros do utilizador
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))
nota5 = float(input("Nota 5: "))


# Calcular a média de 5 valores
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

# Verificar a media
if media >= 9.5:
    print(f"Passou com {media:.2f} valores")
elif 8 <= media < 9.5:
    print(f"Em recuperação com {media:.2f} valores")
else:
    print(f"Reprova com {media:.2f} valores")