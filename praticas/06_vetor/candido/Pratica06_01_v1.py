'''
1. Escreva um programa que leia um vetor contendo N elementos inteiros (N será
lido), calcule e imprima:
• A quantidade de elementos positivos;
• A quantidade de elementos negativos;
• A média dos elementos do vetor.
'''
import random
v = []
pos = 0
neg = 0
n = int(input('Tamanho do vetor: '))
for i in range(n):
    v.append(random.randint(-10,10))
print(*v)
for e in v:
    if e > 0:
        pos += 1
    else:
        neg += 1
media = sum(v) / len(v)
print('Quantidade de elementos positivos:',pos)
print('Quantidade de elementos negativos:',neg)
print('Média dos elementos do vetor:',media)







    
