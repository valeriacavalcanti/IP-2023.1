'''
1. Escreva um programa que leia uma data no
formato “DD/MM/AAAA” e a escreva por extenso.
Por exemplo, se for lida a data “05/06/2023”,
a saída deverá ser “05 de junho de 2023”.
'''
meses = [None,'janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
data = input()
lista = data.split('/')
print(f'{lista[0]} de {meses[int(lista[1])]} de {lista[2]}')

                   
