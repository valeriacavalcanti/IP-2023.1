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
qtd = v.count(k)
print(f'{k} ocorre {qtd} vezes dentro do vetor')
