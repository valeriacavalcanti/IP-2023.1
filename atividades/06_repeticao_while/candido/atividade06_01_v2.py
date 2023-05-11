'''
01. Escreva um programa para ler vários números. O programa
deverá encerrar quando for informado o valor 0 (zero). Ao
final, exiba qual foi o maior número informado.
'''
flag = 0
qtd = 0
while True:
    n = int(input())
    if n == flag:
        break
    qtd = qtd + 1
    if qtd == 1:
        maior = n
    else:
        if n > maior:
            maior = n
if qtd > 0:
    print('Maior =',maior)
else:
    print('Erro')
