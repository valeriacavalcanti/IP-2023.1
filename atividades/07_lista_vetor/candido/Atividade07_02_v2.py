'''
2. Escreva um programa que leia um vetor V (contendo 20
inteiros) e um valor inteiro K, calcule e imprima a
quantidade de ocorrências de K dentro de V.
'''
import random
n = 20
v = []
for i in range(n):
    v.append(random.randint(1,10))
print(v)
k = int(input('Informe o valor a ser procurado: '))
qtd = 0
for e in v:
    if e == k:
        qtd += 1
print(f'{k} ocorre {qtd} vezes dentro do vetor')
