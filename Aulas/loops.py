"""tentativas = 0
mensagem = "Bem Vindo"
password = "password"

for c in range(0,3):
    entrada = input("Insira a password: ")
    if entrada == password:
        print(mensagem)
        break
    else:
        tentativas = tentativas + 1
        print("Tente Novamente \n")
    if tentativas == 3:
        print("Utilizador bloqueado")
        break"""


opcao = 0
while opcao != 4:
    print("[ 1 ] - Registar Pessoa")
    print("[ 2 ] - Nº Pessoas registadas")
    print("[ 3 ] - Apagar um registo")
    print("[ 4 ] - Sair")
    print("Qual a sua opção")
    opcao = int(input("---->"))
    if opcao == 1:
        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a sua idade: "))
        print(f"Olá {nome}")
    elif opcao == 2:
        print("Há x pessoas registadas")
    elif opcao == 3:
        print("Um registo foi apagado")
    elif opcao < 1 or opcao > 4:
        print("F")
        break
print("Obrigado e volte sempre")

