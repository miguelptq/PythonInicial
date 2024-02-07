num = int(input("Numero: "))
contagem = 0
if num != 1 or num != 2 or num != 3 or num != 0:
    for i in range(1, num + 1):
        if num % i == 0:
            contagem += 1
        if contagem > 2:
            break
if contagem > 2 or num == 0:
    print(f"O numero {num} não é primo")
else:
    print(f"O numero {num} é primo")