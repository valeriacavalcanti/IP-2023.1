nome = input()
salario = float(input())
vendas = float(input())

salario_final = salario + vendas * 0.15

print('TOTAL = R$ {:.2f}'.format(salario_final))
