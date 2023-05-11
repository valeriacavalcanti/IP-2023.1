'''
03. A Companhia de Carros Usados João Honesto paga seus
empregados um salário de R$ 1.000,00 por mês mais uma
comissão de R$ 200,00 por cada carro vendido mais 5% do
valor da venda.
Escreva um programa para ler o nome, o número de carros
vendidos e o valor total das vendas de um vendedor,
e calcule e exiba o seu salário final.
'''
SAL_FIXO = 1000.00
COMISSAO = 200.00
PERC = 5/100

nome = input('Nome: ')
num_carros = int(input('Nº de carros vendidos: '))
total_vendas = float(input('Valor total das vendas: R$ '))

sal_final = SAL_FIXO + num_carros*COMISSAO + total_vendas*PERC

print(f'Salário final: R$ {sal_final:.2f}')
