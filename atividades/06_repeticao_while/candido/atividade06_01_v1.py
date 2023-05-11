'''
01. Escreva um programa para ler vários números. O programa
deverá encerrar quando for informado o valor 0 (zero). Ao
final, exiba qual foi o maior número informado.
'''
flag = 0
qtd = 0
n = int(input())
maior = n
while n != flag:
    if n > maior:
        maior = n
    qtd = qtd + 1
    n = int(input())
if qtd > 0:
    print('Maior =',maior)
else:
    print('Erro')
