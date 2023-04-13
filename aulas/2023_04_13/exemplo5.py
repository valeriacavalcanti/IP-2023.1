menor = maior = int(input('Número: '))

for i in range(9):
    num = int(input('Número: '))
    if (num > maior):
        maior = num
    else:
        if (num < menor):
            menor = num

print('Menor =', menor)
print('Maior =', maior)
