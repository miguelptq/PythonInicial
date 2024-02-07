valuesList = list()

while True:
    num = int(input("Digite um número: "))
    if num in valuesList:
        print(f"O numero {num} já se encontra na lista")
    else:
        valuesList.append(num)
        print(f"O número {num} foi inserido com sucesso")
    option = input("Deseja continuar? [S/N]")
    if option.lower() == "N":
        break

valuesList.sort(reverse=True)
print(valuesList)
