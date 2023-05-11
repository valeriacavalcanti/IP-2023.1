soma = 0

for i in range(10):
    num = float(input("Número {}: ".format(i + 1)))
    soma = soma + num

media = soma / 10
print('Média =', media)
