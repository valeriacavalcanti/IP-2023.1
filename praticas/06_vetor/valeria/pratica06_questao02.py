n = int(input("Quantidade: "))
a = [None] * n
b = [None] * n

for i in range(n):
    a[i] = int(input("Valor: "))

k = int(input("Valor de k: "))

for i in range(n):
    b[i] = a[i] * k

print(a)
print(k)
print(b)