'''
04. Um ano bissexto2 possui 366 dias, ou seja, um dia a
mais do que os anos normais. Um ano é considerado bissexto
quando uma das condições é satisfeita:
- É múltiplo de 400;
- É múltiplo de 4 e não é múltiplo de 100.
Escreva um programa para ler um ano (número inteiro) e
informar se este é um ano bissexto.
'''
ano = int(input('Ano: '))
if (ano%400 == 0) or ((ano%4 == 0) and (not ano%100 == 0)):
    print('É bissexto')
else:
    print('Não é bissexto')
