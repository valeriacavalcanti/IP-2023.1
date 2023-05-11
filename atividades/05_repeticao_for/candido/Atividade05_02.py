'''
02. Escreva um programa, em Python, para ler um número
natural (N*), calcular e exibir:
- Os números inteiros entre 1 e esse número lido, inclusive;
- Os divisores desse número;
- Se este é um número primo;
- Se este é um número perfeito ou não;
- Fatorial desse número.
'''

n = int(input('Digite um número natural: '))

#Os números inteiros entre 1 e esse número lido, inclusive;
print(f'\nNúmeros inteiros entre 1 e {n}, inclusive:')
for i in range(1,n+1):
    print(i,end=' ')

#Os divisores desse número;
print(f'\n\nDivisores de {n}:')
for i in range(1,n+1):
    if n % i == 0:
        print(i,end=' ')

#Se este é um número primo;
cont = 0
for i in range(1,n+1):
    if n % i == 0:
        cont = cont + 1
if cont == 2:
    print(f'\n\n{n} é primo')
else:
    print(f'\n\n{n} não é primo')    

#Se este é um número perfeito ou não;
soma = 0
for i in range(1,n):
    if n % i == 0:
        soma = soma + i
if soma == n:
    print(f'\n{n} é um número perfeito')
else:
    print(f'\n{n} não é um número perfeito')    
    
#Fatorial desse número.
fat = 1
for i in range(2,n+1):
    fat = fat * i
print(f'{n}! = {fat}')








