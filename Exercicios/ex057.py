
players = []
while True:
    player = dict()
    player["nome"] = input("Nome do jogador: ")
    player["golos"] = int(input(f"Número de golos do jogador {player['nome']}: "))
    player["numJogos"] = int(input(f"Número de jogos do jogador {player['nome']}: "))
    player["mediaGolos"] = round(player["golos"] / player["numJogos"], 2)
    players.append(player)
    opcao = input("Deseja continuar? [s/n]")
    if opcao == "n":
        break
print()
searchPlayer = input("Nome do jogador que pretende Procurar: ")
print()
for p in players:
    if p["nome"] == searchPlayer:
        print(f"{p['nome']} marcou na média {p['mediaGolos']} golos por jogo")