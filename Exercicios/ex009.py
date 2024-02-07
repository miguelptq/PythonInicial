nome = input("Insira o seu nome:").strip()
print("Maiúsculas: {}".format(nome.upper()))
print("Minúsculas: {}".format(nome.lower()))

print("O seu nome tem {} caracteres".format(len(nome) - nome.count(" ")))

pNome = nome.split()

print("O seu primeiro nome é {} e tem {} caracteres".format(pNome[0], len(pNome[0])))