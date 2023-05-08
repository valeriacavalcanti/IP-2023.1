numeros = [0] * 20

# ler os valores
for i in range(len(numeros)):
    numeros[i] = int(input("Valor {}: ".format(i + 1)))

k = int(input("Valor que deseja buscar: "))

if (k in numeros):
    print("existe")
    for i in range(len(numeros)):
        if (numeros[i] == k):
            print(i)