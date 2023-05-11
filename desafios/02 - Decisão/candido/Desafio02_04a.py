salario = float(input('Salário: R$ '))
if salario <= 400.00:
    perc = 15
if salario > 400.00 and salario <= 800.00:
    perc = 12
if salario > 800.00 and salario <= 1200.00:
    perc = 10
if salario > 1200.00 and salario <= 2000.00:
    perc = 7
if salario > 2000.00:
    perc = 4
reajuste = salario * perc/100
novosal = salario + reajuste
print(f'Novo salario: {novosal:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {perc}%')
