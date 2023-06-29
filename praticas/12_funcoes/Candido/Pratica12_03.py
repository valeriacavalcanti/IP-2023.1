'''
3. Escreva uma função chamada primo para determinar se um número é primo ou não.
   A função deve receber um número inteiro, retornar True se o número for primo,
   ou False caso contrário.
   Escreva também um programa que, usando a função primo criada, imprima os
   números primos entre 1 e 100.
'''
#Função primo
def primo(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

#Programa principal
print('Números primos entre 1 e 100:')
for i in range(1,101):
    if primo(i):
        print(i,end=' ')
