import datetime


def mensagem(msg):
    message = f"   {msg}   "
    total_width = int(len(message) / 2)
    print("-=" * total_width)
    print(message)
    print("-=" * total_width)
    print()


def carta(ano_nascimento):
    """
    -> Esta função retornará se a pessoa está apta para tirar a carta ou não
    :param ano_nascimento: Data de Nascimento da pessoa
    :return: sem retorno
    """
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        return f"Uma pessoa com {idade} anos pode tirar a carta"
    elif idade < 16:
        return f"Uma pessoa com {idade} anos não pode tirar a carta"
    else:
        return f"Uma pessoa com {idade} anos pode tirar a carta com autorização"


mensagem("Carta de condução")
ano = int(input("Digite o seu ano de Nascimento: "))
print(carta(ano))
