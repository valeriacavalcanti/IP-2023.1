'''
1. Faça um programa que leia uma frase e a exiba sem os
espaços em branco.
'''
frase = input('Frase: ')
comp = ''
for caracter in frase:
    if caracter != ' ':
        comp += caracter
print(comp)
