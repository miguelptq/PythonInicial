player = dict()
player["nome"] = input("Nome do jogador: ")
player["golos"] = int(input(f"Número de golos do jogador {player['nome']}: "))
player["numJogos"] = int(input(f"Número de jogos do jogador {player['nome']}: "))
player["mediaGolos"] = round(player["golos"] / player["numJogos"], 2)

print(f"{player['nome']} marcou na média {player['mediaGolos']} golos por jogo")
