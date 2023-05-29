'''
3. Uma matriz transposta é a matriz que se obtém da troca de
linhas por colunas de uma dada matriz.
Assim, dada uma matriz C de ordem m x n, a matriz transposta
dela será representada por Ct de ordem n x m, onde cada
elemento de Ct[i,j] = C[j,i].
Escreva um programa que preencha uma matriz 3x5 com valores
inteiros fornecidos pelo usuário (ou gerados aleatoriamente)
e gere a sua transposta. Ao final, imprima as duas matrizes
(no formato de matriz).
'''
#definição do nº de linhas e de colunas
m = 3
n = 5

#inicialização da matriz C
c = []
for i in range(m):
    c.append([None]*n)

#inicialização da matriz T
t = []
for i in range(n):
    t.append([None]*m)

#geração aleatória da matriz C
import random
for i in range(m):
    for j in range(n):
        c[i][j] = random.randint(1,20)

#geração da matriz T
for i in range(n):
    for j in range(m):
        t[i][j] = c[j][i]

#impressão da matriz C
print('Matriz C')
for i in range(m):
    for j in range(n):
        print(f'{c[i][j]:4}',end='')
    print()

#impressão da matriz T
print('Matriz T')
for i in range(n):
    for j in range(m):
        print(f'{t[i][j]:4}',end='')
    print()
    
    


