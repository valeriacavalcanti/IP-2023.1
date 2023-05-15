vetor = []

while (True):
    num = int(input("Valor: "))
    if (num not in vetor):
        vetor.append(num)
    if (len(vetor) == 6):
        break

print(vetor)