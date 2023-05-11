'''
03. Escreva um programa, em Python, para ler 03 números
(N, X, Y). Calcule e exiba todos os números múltiplos de N
que estão entre X e Y.
'''
n = int(input('Digite o valor de N: '))
x = int(input('Digite o valor de X: '))
y = int(input('Digite o valor de Y: '))
print(f'\nMúltiplos de {n} entre {x} e {y}:') 
if x > y:
    aux = x
    x = y
    y = aux
for i in range(x,y+1):
    if i % n == 0:
        print(i,end=' ')



            
