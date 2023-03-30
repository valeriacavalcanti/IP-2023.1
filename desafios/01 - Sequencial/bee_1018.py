valor = int(input())

c100 = valor // 100
resto = valor % 100

c50 = resto // 50
resto = resto % 50

c20 = resto // 20
resto = resto % 20

c10 = resto // 10
resto = resto % 10

c5 = resto // 5
resto = resto % 5

c2 = resto // 2
c1 = resto % 2

print(valor)
print(c100, 'nota(s) de R$ 100,00')
print(c50, 'nota(s) de R$ 50,00')
print(c20, 'nota(s) de R$ 20,00')
print(c10, 'nota(s) de R$ 10,00')
print(c5, 'nota(s) de R$ 5,00')
print(c2, 'nota(s) de R$ 2,00')
print(c1, 'nota(s) de R$ 1,00')
