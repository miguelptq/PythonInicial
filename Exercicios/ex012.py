print("Vamos iniciar o seu registo")

nome = input("Digite o seu primeiro e ultimo nome: ").strip()
#Encontrar o indicedo espaço em branco no nome

indice_espaco = nome.find(" ")

# Guarda a primeira letra do primeiro nme em minuscula

primeira_letra = nome[0].lower()

# Guardar as letras apos o espaco (ultimo nome) em minusculas

ultimo_nome = nome[indice_espaco + 1:].lower()

email = f"{primeira_letra}.{ultimo_nome}.edu@empresa.pt"

# Imprimir o email com as inciais esem espaco apos o ponto

print(f"Nome: {nome}")
print(f"Email: {email}")