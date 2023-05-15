vetor = [None] * 6

for i in range(6):
    vetor[i] = int(input("Valor: "))

for i in range(6):
    if (vetor.count(vetor[i]) ==  1):
        print(i, vetor[i], 'é distinto')
    else:
        print(i, vetor[i], 'não é distinto')