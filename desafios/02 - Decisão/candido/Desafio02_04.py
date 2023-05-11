salario = float(input('Salário: R$ '))
if salario <= 400.00:
    perc = 15
elif salario <= 800.00:
    perc = 12
elif salario <= 1200.00:
    perc = 10
elif salario <= 2000.00:
    perc = 7
else:
    perc = 4
reajuste = salario * perc/100
novosal = salario + reajuste
print(f'Novo salario: {novosal:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {perc}%')
