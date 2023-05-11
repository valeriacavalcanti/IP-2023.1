'''
1. Escreva um programa que leia 10 números inteiros e
armazene-os em um vetor.
Imprima:
• Os números que estão nos índices pares;
• Os números que estão nos índices ímpares.
'''
n = 6
v = []
vp = []
vi = []
print(f'Digite {n} números:')
for i in range(n):
    v.append(int(input()))
    if i % 2 == 0:
        vp.append(v[i])
    else:
        vi.append(v[i])
print('Números que estão nos índices pares:')
for e in vp:
    print(e)
print('Números que estão nos índices ímpares:',vi)
for e in vi:
    print(e)




