'''
04. Escreva uma função chamada fatorial que receba
    um número inteiro e retorne seu fatorial. Faça
    também um programa para testar a função.
'''
def fatorial(n):
    if n < 0:
        return None
    f = 1
    for i in range(2,n+1):
        f *= i
    return f

import math
num = int(input('Digite um número inteiro positivo: '))
fat = fatorial(num)
print(f'{num}! = {fat}')
fat2 = math.factorial(num)
print(f'{num}! = {fat2}')

