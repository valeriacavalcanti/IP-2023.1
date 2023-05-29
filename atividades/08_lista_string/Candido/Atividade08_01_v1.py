'''
1. Escreva um programa que leia uma frase e a exiba
“na vertical”, ou seja, com uma letra em cada linha.
'''

frase = input('Frase: ')
for i in range(len(frase)):
    print(frase[i])
