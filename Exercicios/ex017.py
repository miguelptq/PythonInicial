# Pedir numero de utilizador
number = int(input("Numero: "))
print("\n:::: Escolha uma opção ::::\n")

# Opção escolhida
option = int(input("[ 1 ] - Binário \n[ 2 ] - Octal \n[ 3 ] - Hexadecimal \n\nQual a sua opção: "))

# mostrar base de conversão
if option == 1:
    print(f"O número {number} convertido para binario fica com o valor de {bin(number)[2::+1]}")
elif option == 2:
    print(f"O número {number} convertido para octal fica com o valor de {oct(number)[2::+1]}")
elif option == 3:
    print(f"O número {number} convertido para hexadecimal fica com o valor de {hex(number)[2::+1].upper()}")
else:
    print("Tente novamente. Por favor insira uma opção válida")