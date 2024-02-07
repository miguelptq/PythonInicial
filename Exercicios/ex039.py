equipas = ("Real Madrid", "Girona", "Atético Madrid", "Barcelona", "Athletic Club", "Real Sociedad", "Real Betis",
           "Getafe", "Valencia", "Las Palmas", "Rayo Vallecano", "Osasuna", "Villareal", "Mallorca",
           "Desportivo Alavés", "Sevilla", "Celta de Vigo", "Cádiz", "Granada", "Almeria")
print("Primeiros 5: ")
for e in equipas[0:5]:
    print(f"{equipas.index(e) + 1}º lugar -> {e}")
print("\n\nUltimos 4 classificados: ")
for e in equipas[-4:]:
    print(f"{equipas.index(e) + 1}º lugar -> {e}")

print("\n\nLista de equipas por ordem alfabética:")
ordemAlfabetica = sorted(equipas)
count = 0
for e in ordemAlfabetica:
    print(e)

print(f"A equipa Sevilla encontra-se na posição: {equipas.index("Sevilla") + 1}º")