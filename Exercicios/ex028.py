pergunta = input("Ola123? ").lower()
while pergunta not in 'vf':
    pergunta = input("Volte a tentar, V ou F: ").lower()
if pergunta == 'v':
    print("Certo")
else:
    print("Errou")

pergunta = input("Ola1234? ").lower()
while pergunta not in 'vf':
    pergunta = input("Volte a tentar, V ou F: ").lower()
if pergunta == 'f':
    print("Certo")
else:
    print("Errou")

pergunta = input("Ola123456? ").lower()
while pergunta not in 'vf':
    pergunta = input("Volte a tentar, V ou F: ").lower()
if pergunta == 'f':
    print("Certo")
else:
    print("Errou")