'''
4. Escreva um programa que receba um vetor V de N números
inteiros distintos (N será lido), determine e exiba o maior
e o menor elemento deste vetor e seus respectivos índices.
'''
import random
v = []
n = int(input('Digite o tamanho do vetor: '))
print(f'Digite os {n} elementos do vetor:')
for i in range(n):
    v.append(int(input(f'v[{i}]: ')))
maior = max(v)
indmaior = v.index(maior)
menor = min(v)
indmenor = v.index(menor)
print('Maior =',maior,'Índice =',indmaior)
print('Menor =',menor,'Índice =',indmenor)
