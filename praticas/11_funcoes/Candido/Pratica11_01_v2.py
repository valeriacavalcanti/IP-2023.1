'''
01. Escreva uma função chamada menor que receba
    3 números e retorne o menor deles. Faça
    também um programa para testar a função.
'''
def menor(a,b,c):
    m = a
    if b < m:
        m = b
    if c < m:
        m = c
    return m

print('Digite 3 números inteiros:')
n1 = int(input())
n2 = int(input())
n3 = int(input())
print('O menor é',menor(n1,n2,n3))

        
    
