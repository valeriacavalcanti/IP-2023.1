'''
4. Escreva um programa que receba um vetor V de N números
inteiros distintos (N será lido), determine e exiba o maior
e o menor elemento deste vetor e seus respectivos índices.
'''
v = []
n = int(input('Digite o tamanho do vetor: '))
print(f'Digite os {n} elementos do vetor:')
for i in range(n):
    v.append(int(input(f'v[{i}]: ')))
maior = menor = v[0]
indmaior = indmenor = 0
for i in range(1,n):
    if v[i] > maior:
        maior = v[i]
        indmaior = i
    if v[i] < menor:
        menor = v[i]
        indmenor = i
print('Maior =',maior,'Índice =',indmaior)
print('Menor =',menor,'Índice =',indmenor)
