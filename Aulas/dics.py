#aluno = [{"nome": "Cesar", "media": 14}, {"nome": "Miguel", "media": "13"}]
cidade = {"nome": "Porto", "codigo": "OPO", "baixa": "Ribeira", "rio": "Douro"}
cidade2 = {"nome": "Lisboa", "codigo": "LX", "baixa": "Chiado", "rio": "Tejo"}
pais =  list()
pais.append(cidade)
pais.append(cidade2)
for c in range(len(pais)):
    print(f"{pais[c]['nome']}")

"""for k,v in cidade.items():
    print(f"{k} é {v}")
print(cidade)"""
"""aluno = dict()

aluno["nome"] = input("Digite o nome do aluno:")
aluno["Ex001"] = int(input("Digite o nota do ex001: "))
aluno["Ex002"] = int(input("Digite o nota do ex002: "))
aluno["Ex003"] = int(input("Digite o nota do ex003: "))

aluno["media"] = (aluno["Ex001"] + aluno["Ex002"] + aluno["Ex003"]) / 3

del aluno["media"]


print(aluno.items())"""
