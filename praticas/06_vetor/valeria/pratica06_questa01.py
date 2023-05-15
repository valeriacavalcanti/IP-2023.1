n = int(input("Quantidade: "))
vetor = [None] * n

# ler os valores
for i in range(n):
    vetor[i] = int(input("Valor: "))

positivos = 0
negativos = 0
soma = 0
for i in range(n):
    soma += vetor[i]
    if (vetor[i] > 0):
        positivos += 1  # positivos = positivos + 1
    elif (vetor[i] < 0):
        negativos += 1

print(vetor)
print(positivos)
print(negativos)
media = soma / n
print(media)