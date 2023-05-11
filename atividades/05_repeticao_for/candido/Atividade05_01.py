'''
01. Escreva um programa, em Python, para ler 10 números.
Calcular e exibir a média dos números lidos.
'''
qtd = 3
soma = 0
print(f'Digite {qtd} números:')
for i in range(qtd):
    num = float(input())
    soma = soma + num
media = soma / qtd
print(f'Média = {media:.2f}')
