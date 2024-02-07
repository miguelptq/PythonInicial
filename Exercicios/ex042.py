jogos = ( "Nioh - Playstation Hits PS4", 19.99,
          "Marvel's Spider-Man: Miles Morales PS4", 59.99,
          "Marvel's Spider-Man PS4", 24.99,
          "The Last of Us Remastered - PS4", 19.99,
          "Minecraft - Starter Collection PS4", 26.99,
          "Gran Turismo 7 - Standard Edition PS4", 69.99,
          "Hogwarts Legacy PS4", 39.99,
          "Elden Ring - Standard Edition PS4", 59.99
          )

print("-" * 55)
print(f'{"LISTA DE JOGOS":^55}')
print("-" * 55)

for pos in range(0, len(jogos)):
    if pos % 2 == 0:
        print(f"{jogos[pos]:-<45}", end=" ")
    else:
        print(f"{jogos[pos]:>7.2f}€")
print("_" * 55)