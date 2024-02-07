numList = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, len(numList)):
    for j in range(0, len(numList[i])):
        numList[i][j] = int(input(f"Digite um valor para [{i}][{j}]: "))

for i in range(0, len(numList)):
    for j in range(0, len(numList[i])):
        print(numList[i][j], end=" ")
    print("")