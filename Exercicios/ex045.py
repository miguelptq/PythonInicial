valuesList = list()
maxValuesList = 0
for i in range(0, 5):
    num = int(input("Digite um número: "))
    if i == 0:
        valuesList.append(num)
        print(f"O número {num} foi adicionado na última posição")
    #elif num in valuesList:
        #print(f"O número {num} já se encontra na lista")
    else:
        index = 0
        while index < len(valuesList) and valuesList[index] < num:
            index += 1
        valuesList.insert(index, num)
        if index == len(valuesList) - 1:
            print(f"O número foi adicionado na última posição, posição {index}")
        else:
            print(f"O número  {num} foi inserido na posição {index}")
print(f"Lista de número ordenado: {valuesList}")
