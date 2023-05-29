'''
2. Escreva um programa que leia uma frase e determine a
quantidade de brancos contidos na mesma.
'''
frase = input('Frase: ')
cont = 0
for caracter in frase:
    if caracter == ' ':
        cont += 1
print('Quantidade de brancos:',cont)
