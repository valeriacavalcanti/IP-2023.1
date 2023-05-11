'''
04. Escreva um programa para ler vários números inteiros.
O programa deverá encerrar quando for informado um valor
negativo ou zero. Para cada número lido o programa deverá
exibir todos os divisores desse respectivo número.
Ao final, o programa deverá exibir quantos números foram
informados.
'''
cont = 0
while True:
    n = int(input())
    if n <= 0:
        break
    cont = cont + 1
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end=' ')
    print()
print('Números informados:',cont)
    
