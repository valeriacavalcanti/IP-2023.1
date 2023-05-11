'''
3. Escreva um programa que leia um vetor V (contendo 20
inteiros) e um valor inteiro K, verifique e imprima se o K
está ou não no vetor. Se estiver, informe em que posição
(index).
Obs: K pode se repetir no vetor, nesse caso, mostre todas as
posições onde o K aparece.
'''
import random
n = 10
v = []
for i in range(n):
    v.append(random.randint(1,10))
print(v)
k = int(input('Informe o valor a ser procurado: '))
if k in v:
    print(f'O valor {k} aparece no vetor nos índices:')
    for i in range(n):
        if v[i] == k:
            print(i)
else:
    print(f'O valor {k} não aparece no vetor')
