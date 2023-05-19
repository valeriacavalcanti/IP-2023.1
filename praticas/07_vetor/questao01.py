n = int(input("Quantidade: "))
lista = []

for i in range(n):
    lista.append(int(input("Valor: ")))

print(lista)

for i in range(n//2):
    lista[i], lista[n-1-i] = lista[n-1-i], lista[i]

print(lista)
