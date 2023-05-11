numeros = [0] * 20
qtd = 0

# ler os valores
for i in range(len(numeros)):
    numeros[i] = int(input("Valor {}: ".format(i + 1)))

k = int(input("Valor que deseja buscar: "))

# contar a frequencia de K
for i in range(len(numeros)):
    if (numeros[i] == k):
        qtd = qtd + 1

print(qtd, numeros.count(k))