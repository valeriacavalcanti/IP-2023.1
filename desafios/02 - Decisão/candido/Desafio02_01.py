import math
print('Entre com os coeficientes a, b e c')
a = float(input())
b = float(input())
c = float(input())
delta = b ** 2 - 4 * a * c
if delta < 0 or a == 0:
    print('Impossível calcular')
else:    
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'x1 = {x1:.5f}')
    print(f'x2 = {x2:.5f}')

