'''
2. Faça um programa que leia uma frase e a exiba com a
inicial de cada palavra em maiúsculo.
'''
frase = input('Frase: ')
lista = frase.split()
for palavra in lista:
    print(palavra[0].upper(),palavra[1:],sep='',end=' ')
