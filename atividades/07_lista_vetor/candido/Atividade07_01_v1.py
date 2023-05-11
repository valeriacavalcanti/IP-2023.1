'''
1. Escreva um programa que leia 10 números inteiros e
armazene-os em um vetor.
Imprima:
• Os números que estão nos índices pares;
• Os números que estão nos índices ímpares.
'''
n = 6
v = []
print(f'Digite {n} números:')
for i in range(n):
    v.append(int(input()))
print('Números que estão nos índices pares:')
for i in range(0,n,2):
    print(v[i])
print('Números que estão nos índices ímpares:')
for i in range(1,n,2):
    print(v[i])
