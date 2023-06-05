'''
2. Escreva um programa que leia o nome completo
de uma pessoa e imprima um login baseado na
seguinte regra: o primeiro nome seguido por um
ponto e pelo último sobrenome, tudo em minúsculo.
Obs: considere que o nome a ser digitado não
contém preposições nem artigos.
Por exemplo, se for lido o nome:
“Antonio Carlos Ferreira Santos”,
deverá ser impresso o login:
“antonio.santos”
'''
nome = input().lower()
lista = nome.split()
print(lista[0],lista[-1],sep='.')
