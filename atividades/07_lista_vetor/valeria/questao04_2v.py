numeros = []
qtd = int(input("Quantidade: "))

while (len(numeros) < qtd):
    num = int(input("Número: "))
    if (num not in numeros):
        numeros.append(num)

p_maior = p_menor = 0

for i in range(1, len(numeros)):
    if (numeros[i] > numeros[p_maior]):
        p_maior = i
    elif (numeros[i] < numeros[p_menor]):
        p_menor = i

print(numeros)
print(p_menor, numeros[p_menor])
print(p_maior, numeros[p_maior])