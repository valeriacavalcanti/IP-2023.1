import random

n = int(input("Ordem da matriz quadrada: "))

matriz = []
for i in range(n):
    matriz.append([None] * n)

for i in range(n):
    for j in range(n):
        matriz[i][j] = random.randint(1,10)

# exibir todos os elementos da matriz, no formato matriz
for i in range(n):
    for j in range(n):
        print("{:2}".format(matriz[i][j]), end=' ')
    print()

# exibir os elementos que estão na diagonal principal
for i in range(n):
    for j in range(n):
        if (i == j):
            print("{:2}".format(matriz[i][j]), end=' ')
        else:
            print("  ".format(matriz[i][j]), end=' ')
    print()