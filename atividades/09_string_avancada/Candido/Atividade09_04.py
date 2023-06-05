'''
4. Escreva um programa que leia uma palavra e
imprima a quantidade de repetições de cada letra
contida na palavra.
Por exemplo, se a palavra lida for “PROGRAMA”,
deverá ser impresso:
P - 1
R - 2
O - 1
G - 1
A - 2
M - 1
'''
palavra = input()
comp = ''
for caracter in palavra:
    if caracter not in comp:
        comp += caracter
for caracter in comp:
    cont = palavra.count(caracter)
    print(caracter,'-',cont)





