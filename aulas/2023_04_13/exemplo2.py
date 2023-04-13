pos = neg = zero = 0

for i in range(10):
    num = int(input("Número: "))
    if (num > 0):
        pos = pos + 1
    elif (num < 0):
        neg = neg + 1
    else:
        zero = zero + 1

print('Positivos:', pos)
print('Negativos:', neg)
print('Zero:', zero)
