def max_value(*nums):
    max_val = 0
    for v in nums[0]:
        if v > max_val:
            max_val = v
    print(f"O valor máximo é: {max_val}")


numList = list()
while True:
    num = int(input("Digite um número: "))
    numList.append(num)
    opcao = input("Deseja continuar? [s/n]")
    if opcao == "n":
        break

max_value(numList)
