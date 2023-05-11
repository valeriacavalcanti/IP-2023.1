numeros = []
qtd = int(input("Quantidade: "))

while (len(numeros) < qtd):
    num = int(input("Número: "))
    if (num not in numeros):
        numeros.append(num)

maior = menor = numeros[0]
p_maior = p_menor = 0

for i in range(1, len(numeros)):
    if (numeros[i] > maior):
        maior = numeros[i]
        p_maior = i
    elif (numeros[i] < menor):
        menor = numeros[i]
        p_menor = i

print(numeros)
print(p_menor, menor)
print(p_maior, maior)