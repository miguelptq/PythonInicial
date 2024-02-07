from random import randint
from time import sleep
import operator
players = {
    "Miguel": randint(1, 6),
    "Alfredo": randint(1, 6),
    "Cesar": randint(1, 6),
    "Zé": randint(1, 6),
    "Ricardo": randint(1, 6)
}
for n, p in players.items():
    print(f"O jogador {n} tirou {p}")
    sleep(0.4)
print("=-"*30)
print("RANKING")
print("=-"*30)
sorted_players = dict(sorted(players.items(), key=operator.itemgetter(1), reverse="True"))
for n, p in sorted_players.items():
    print(f"{n} com {p}")
    sleep(0.4)
