'''
01. Escreva um programa, em Python, para ler 02(dois)
números naturais (N∗). Calcular e exibir o maior valor
entre os dois.
'''
print('Digite dois números naturais:')
a = int(input())
b = int(input())
if a < b:
    maior = b
else:
    maior = a
print(maior)
