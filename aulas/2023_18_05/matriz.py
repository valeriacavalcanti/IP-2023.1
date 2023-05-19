# matriz 6 x 4

# declarar a matriz
matriz = []
for i in range(6):
    matriz.append([0] * 4)

print(matriz)
matriz[1][0] = 100
print(matriz)

# imprimir a matriz, por linha
for i in range(6):
    print(matriz[i])

# imprimir a matriz por elemento
for i in range(6):
    for j in range(4):
        print(i, j, matriz[i][j])
