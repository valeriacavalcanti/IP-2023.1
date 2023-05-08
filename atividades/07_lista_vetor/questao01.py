numeros = [0] * 10

# ler os valores
for i in range(10):
    numeros[i] = int(input("Valor {}: ".format(i + 1)))

# exibir os índices pares
for i in range(0, 10, 2):
    print(numeros[i])

# exibir os índices ímpares
for i in range(1, 10, 2):
    print(numeros[i])