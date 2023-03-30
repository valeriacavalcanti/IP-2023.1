PI = 3.14159

num1, num2, num3 = input().split()
num1, num2, num3 = float(num1), float(num2), float(num3)

triangulo = (num1 * num3) / 2
circulo = PI * (num3 ** 2)
trapezio = ((num1 + num2) * num3) / 2
quadrado = num2 ** 2
retangulo = num1 * num2

print('TRIANGULO = {:.3f}'.format(triangulo))
print('CIRCULO = {:.3f}'.format(circulo))
print('TRAPEZIO = {:.3f}'.format(trapezio))
print('QUADRADO = {:.3f}'.format(quadrado))
print('RETANGULO = {:.3f}'.format(retangulo))
