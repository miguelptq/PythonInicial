while True:
    num = int(input("Número: "))
    if num <= 0:
        print("Programa terminado!!")
        break
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
