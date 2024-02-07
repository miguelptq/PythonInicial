#Crie um programa onde o utilizador possa inserir uma equação matemática que use parênteses.
# O programa deverá analisar a equação e dizer se a equação tem os parênteses corretos ou se está errado.
print("Digite uma equação:")
equacao = input("--->")
#PDireita = (
#PEsquerda = )
contagemPDireita = 0
contagemPEsquerda = 0
for i in equacao:
    if i == "(":
        contagemPDireita += 1
    if i == ")":
        contagemPEsquerda += 1
if contagemPDireita == contagemPEsquerda:
    print("Equação está correta")
else:
    print("A equação está errada")
