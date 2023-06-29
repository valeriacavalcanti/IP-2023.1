from questao_02_funcoes import *

ordem = int(input("Ordem: "))

matriz1 = criar_matriz(ordem)
matriz2 = criar_matriz(ordem)

preencher_matriz(matriz1)
preencher_matriz(matriz2)

matriz_r = somar_matriz(matriz1, matriz2)
print_matriz(matriz_r)
