pos = neg = par = impar = 0

for i in range(5):
    num = int(input())
    if (num % 2 == 0):
        par = par + 1
    else:
        impar = impar + 1

    if (num > 0):
        pos = pos + 1
    elif (num < 0):
        neg = neg + 1

print(par, 'valor(es) par(es)')
print(impar, 'valor(es) impar(es)')
print(pos, 'valor(es) positivo(s)')
print(neg, 'valor(es) negativo(s)')
