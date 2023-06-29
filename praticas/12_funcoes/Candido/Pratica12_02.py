'''
2. Escreva um programa que leia duas matrizes de inteiros e gere uma terceira
   matriz que corresponderá a soma das duas matrizes lidas. A ordem das matrizes
   também será lida. Imprima as três matrizes.
   O programa deverá conter as seguintes funções:
   • Uma função para gerar e ler uma matriz, sendo passados como parâmetros a
     ordem da matriz.
   • Uma função para exibir uma matriz em sua representação clássica (linhas e
     colunas).
   • Uma função para somar duas matrizes.  
'''
# Função para gerar e ler uma matriz
def lerMat(nl,nc):
    m = []
    for i in range(nl):
        m.append([None] * nc)
        for j in range(nc):
            m[i][j] = int(input())
    return m

# Função para somar duas matrizes
def somaMat(a,b):
    nl = len(a)
    nc = len(b[0])
    c = [[None]*nc for i in range(nl)]
    for i in range(nl):
        for j in range(nc):
            c[i][j] = a[i][j] + b[i][j]
    return c

# Função para imprimir uma matriz
def impMat(m):
    nl = len(m)
    nc = len(m[0])
    for i in range(nl):
        for j in range(nc):
            print(f'{m[i][j]:4}',end='')
        print()

#Programa principal
print('Informe a ordem da matriz:')
nlin = int(input('Nº de linhas: '))
ncol = int(input('Nº de colunas: '))
print('\nDigite os elementos da 1ª matriz:')
m1 = lerMat(nlin,ncol)
print('\nDigite os elementos da 2ª matriz:')
m2 = lerMat(nlin,ncol)
ms = somaMat(m1,m2)
print('\n1ª Matriz:')
impMat(m1)
print('\n2ª Matriz:')
impMat(m2)
print('\nMatriz Soma:')
impMat(ms)
