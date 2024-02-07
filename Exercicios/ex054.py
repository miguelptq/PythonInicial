import datetime

simulador = dict()
simulador["nome"] = input("Qual o seu nome? ")
simulador["anoNasc"] = int(input("Em que ano nasceu? "))
simulador["rendimentos"] = float(input("Quais os seus rendimentos mensais? "))
simulador["despesasMensais"] = float(input("Valor das despesas mensais? "))
simulador["montanteCredito"] = float(input("Montante Crédito: "))
simulador["prazoAnos"] = int(input("Prazo em anos: "))
currentYear = datetime.date.today().year
simulador["idade"] = currentYear - simulador["anoNasc"]
del simulador["anoNasc"]
simulador["remanescente"] = simulador["rendimentos"] - simulador["despesasMensais"]
meses = simulador["prazoAnos"] * 12
simulador["credito_mensal"] = round(simulador["montanteCredito"] / meses,2)
simulador["aprovado"] = "Não"
print("=-"*30)
print("Resultados")
print("=-"*30)
if simulador["remanescente"] > simulador["credito_mensal"]:
    simulador["aprovado"] = "Sim"
#print(simulador)

for k, s in simulador.items():
    if (k == "montateCredito" or k == "despesasMensais" or k == "remanescente" or k == "credito_mensal" or
            k == "rendimentos" or k == "montanteCredito"):
        s = str(s) + "€"
    print(f"{k} : {s}")
