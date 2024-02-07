num = int(input("Numero: "))
count = 0
ultimo = 1
penultimo = 1
resultado = ""
while count < num:
    if count == 0 or count == 1:
        termo = 1
        resultado += f"{termo}~"
    else:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        resultado += str(termo) + "~"
    count += 1
resultadoFinal = resultado[:-1]
print(resultadoFinal)