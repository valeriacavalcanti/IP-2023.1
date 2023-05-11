numeros = [0] * 20
indices = []

# ler os valores
for i in range(len(numeros)):
    numeros[i] = int(input("Valor {}: ".format(i + 1)))

k = int(input("Valor que deseja buscar: "))

if (k in numeros):
    for i in range(len(numeros)):
        if (numeros[i] == k):
            indices.append(i)
    print(indices)