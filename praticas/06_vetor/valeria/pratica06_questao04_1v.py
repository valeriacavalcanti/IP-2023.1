vetor = []

while (len(vetor) < 6):
    num = int(input("Valor: "))
    if (num not in vetor):
        vetor.append(num)

print(vetor)