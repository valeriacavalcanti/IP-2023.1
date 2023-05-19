n = int(input("Quantidade: "))
lista = []
distintos = []
freq = []

# ler os valores da lista
for i in range(n):
    lista.append(int(input("Valor: ")))

# calcular a frequência dos valores distintos
for i in range(n):
    if (lista[i] not in distintos):
        distintos.append(lista[i])
        freq.append(lista.count(lista[i]))

# calcular a maior frequência
maior = -1
for i in range(len(freq)):
    if (freq[i] > maior):
        maior = freq[i]

# exibir os "donos" da maior frequência
for i in range(len(freq)):
    if (freq[i] == maior):
        print(distintos[i])
