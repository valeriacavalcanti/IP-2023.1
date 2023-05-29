'''
Escreva um programa que preencha duas matrizes (A e B), ambas
de ordem 2x3, com valores inteiros fornecidos pelo usuário
(ou gerados aleatoriamente). O programa deverá somar as
duas matrizes, armazenando o resultado em uma terceira matriz
(C). Ao final, exiba as 3 matrizes (no formato de matriz).
'''
import random

#definição da ordem das matrizes
nlin = 2
ncol = 3

#inicialização da matriz A
a = []
for i in range(nlin):
    a.append([0]*ncol)

#inicialização da matriz B
b = []
for i in range(nlin):
    b.append([0]*ncol)

#inicialização da matriz C
c = []
for i in range(nlin):
    c.append([0]*ncol)

#geração aleatória da matriz A
for i in range(nlin):
    for j in range(ncol):
        a[i][j] = random.randint(1,20)

#geração aleatória da matriz B
for i in range(nlin):
    for j in range(ncol):
        b[i][j] = random.randint(1,20)

#cálculo da matriz C = A + B
for i in range(nlin):
    for j in range(ncol):
        c[i][j] = a[i][j] + b[i][j]
        
#impressão da matriz A
print('Matriz A:')
for i in range(nlin):
    for j in range(ncol):
        print(f'{a[i][j]:3}',end=' ')
    print()

#impressão da matriz B
print('Matriz B:')
for i in range(nlin):
    for j in range(ncol):
        print(f'{b[i][j]:3}',end=' ')
    print()

#impressão da matriz C = A + B
print('Matriz C = A + B:')
for i in range(nlin):
    for j in range(ncol):
        print(f'{c[i][j]:3}',end=' ')
    print()






    



