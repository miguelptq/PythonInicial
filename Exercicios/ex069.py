def mensagem(msg):
    message = f"   {msg}   "
    total_width = int(len(message) / 2)
    print("-=" * total_width)
    print(message)
    print("-=" * total_width)
    print()

def calcular_imc(age, weight, height):
    """
    -> esta função serve para calcular o imc
    :param age: idade da pessoa
    :param weight:  peso da pessoa
    :param height:  altura da pessoa
    :return: retorna o imc da pessoa
    """
    i = round(peso / (altura * altura), 2)
    return i


def imc_data(valor):
    """
    -> esta função informa se o utilizador esta sobre o peso, peso normal, etc..
    :param valor: imc do utilizador
    :return: valor associado ao imc
    """
    valor_imc = ""
    if valor < 18.5:
        valor_imc = "Abaixo do peso"
    elif valor <= 24.9:
        valor_imc = "Peso normal"
    elif valor <= 29.9:
        valor_imc = "Sobrepeso"
    elif valor <= 34.9:
        valor_imc = "Obesidade grau 1"
    elif valor <= 39.9:
        valor_imc = "Obesidade grau 2"
    elif valor >= 40.0:
        valor_imc = "Obesidade mórbida"
    return valor_imc


mensagem("Calculador de IMC")
idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
if altura >= 3:
    altura = altura / 100

imc = calcular_imc(idade, peso, altura)
imc_dados = imc_data(imc)

print(f"O utilizador encontra-se no grau: {imc_dados}")
