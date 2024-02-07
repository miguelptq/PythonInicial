def mensagem(msg):
    message = f"   {msg}   "
    total_width = int(len(message) / 2)
    print("-=" * total_width)
    print(message)
    print("-=" * total_width)
    print()

def calculador_notas(*notas):
    """
    -> esta função ira determinar a media, a maior, a menor e a quantidade de notas
    :param notas: lista de notas dos alunos
    :return: dicionario de vários valores
    """
    notas_dict = dict()
    soma = 0
    notas_dict["quantidade"] = len(notas[0])
    notas_dict["maior"] = max(notas[0])
    notas_dict["menor"] = min(notas[0])
    for n in notas[0]:
        soma += n
    notas_dict["media"] = soma / len(notas[0])
    return notas_dict


def calc_situacao(media):
    if media > 12:
        s = "Boa"
    elif media < 9.5:
        s = "Fraca"
    else:
        s = "Razoável"
    return s


lista_notas = []
while True:
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)
    opcao = input("Deseja adicionar mais notas? [S/N]").lower().strip()
    if opcao == "n":
        break
notas_data = calculador_notas(lista_notas)
situacao = calc_situacao(notas_data["media"])

print()
print(f"Quantiade de notas: {notas_data['quantidade']}")
print(f"Maior nota: {notas_data['maior']}")
print(f"Menor nota: {notas_data['menor']}")
print(f"Situação: {situacao}")
