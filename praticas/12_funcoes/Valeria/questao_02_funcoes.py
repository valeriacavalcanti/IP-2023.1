def criar_matriz(linhas, colunas = -1):
    if (colunas == -1):
        colunas = linhas
    matriz = []
    for i in range(linhas):
        matriz.append([0] * colunas)
    return matriz

def preencher_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Valor({i},{j}): "))

def print_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print("{:>02d}".format(matriz[i][j]), end=' ')
        print()

def somar_matriz(matriz1, matriz2):
    matriz3 = criar_matriz(len(matriz1))
    for i in range(len(matriz3)):
        for j in range(len(matriz3[i])):
            matriz3[i][j] = matriz1[i][j] + matriz2[i][j]
    return matriz3
