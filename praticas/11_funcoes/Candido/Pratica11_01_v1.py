'''
01. Escreva uma função chamada menor que receba
    3 números e retorne o menor deles. Faça
    também um programa para testar a função.
'''
def menor(a,b,c):
    if a < b and a < c:
        return a
    else:
        if b < c:
            return b
        else:
            return c

print('Digite 3 números inteiros:')
n1 = int(input())
n2 = int(input())
n3 = int(input())
m = menor(n1,n2,n3)
print('O menor é',m)

        
    
