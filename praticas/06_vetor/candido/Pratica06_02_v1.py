'''
2. Escreva um programa que leia um vetor A de N números
inteiros (N será lido) e um outro inteiro K, construa e
imprima um outro vetor B cujos elementos são os respectivos
elementos de A multiplicados por K.
Ex: A = [1,2,3], K = 5, B = [5,10,15].
'''
a = []
b = []
n = int(input('Digite o tamanho do vetor: '))
print('Digite os elementos do vetor A:')
for i in range(n):
    a.append(int(input(f'A[{i}]: ')))
k = int(input('Valor de K: '))
for i in range(n):
    b.append(a[i]*k)
print('A =',*a)
print('K =',k)
print('B =',*b)
