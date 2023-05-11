'''
O restaurante a quilo Bem-Bão cobra R$25,00 por cada quilo
de refeição. Escreva um programa para ler o peso do prato
montado pelo cliente (em quilos) e exiba o valor a pagar.
Assuma que a balança já desconte o peso do prato.
'''
KG = 25.00
peso = float(input('Peso do prato (em Kg): '))
total = peso * KG
print(f'Valor a pagar: R$ {total:.2f}')
