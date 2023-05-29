'''
2. Escreva um programa que:
• Leia (ou gere aleatoriamente) uma matriz quadrada de ordem N
  contendo elementos inteiros (N será lido);
• Exiba a matriz lida (no formato de matriz);
• Exiba os elementos da diagonal principal, isto é, os
  elementos onde I = J.
'''
n = int(input('Ordem da matriz: '))

matriz = []
for i in range(n):
    matriz.append([0]*n)

import random
for i in range(n):
    for j in range(n):
        matriz[i][j] = random.randint(1,20)

print('Matriz:')
for i in range(n):
    for j in range(n):
        print(f'{matriz[i][j]:4}',end='')
    print()

print('Diagonal principal:')
for i in range(n):
    for j in range(n):
        if i == j:
            print(f'{matriz[i][j]:4}',end='')


    





            
