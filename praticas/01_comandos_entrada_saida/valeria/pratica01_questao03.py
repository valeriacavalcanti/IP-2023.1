SALARIO = 1000

nome = input("Nome: ")
quantidade = int(input("Quantidade: "))
valor = float(input("Valor das vendas: "))

salario_final = SALARIO + (200 * quantidade) + (valor * 0.05)

print('Salário final =', salario_final)
