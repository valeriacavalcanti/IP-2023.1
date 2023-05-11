salario = float(input())

if (salario <= 400):
    reajuste = 15
elif (salario <= 800):
    reajuste = 12
elif (salario <= 1200):
    reajuste = 10
elif (salario <= 2000):
    reajuste = 7
else:
    reajuste = 4

aumento = salario * reajuste / 100
novo_salario = salario + aumento

print('Novo salario: {:.2f}'.format(novo_salario))
print('Reajuste ganho: {:.2f}'.format(aumento))
print('Em percentual: {} %'.format(reajuste))
