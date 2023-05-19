n = int(input("Quantidade: "))
a = []
b = []
c = []

for i in range(n):
    a.append(int(input("Valor: ")))

for i in range(n):
    b.append(int(input("Valor: ")))

for i in range(n):
    c.append(a[i])
    c.append(b[i])

print(a)
print(b)
print(c)
