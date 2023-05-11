'''
03. Escreva um programa para obter a data de nascimento
(dia, mês e ano) de uma pessoa. Calcular e exibir a idade
dessa pessoa. Considere a data 30/03/2023 como referência.
'''
print('Informe a data de nascimento (dia, mês e ano)')
dia = int(input())
mes = int(input())
ano = int(input())
if (mes > 3) or (mes == 3 and dia > 30):
    idade = 2023 - ano - 1
else:
    idade = 2023 - ano
print(idade)
