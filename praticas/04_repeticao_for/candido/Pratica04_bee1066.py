imp = 0
par = 0
pos = 0
neg = 0
for i in range(5):
    n = int(input())
    if n % 2 == 0:
        par = par + 1
    else:
        imp = imp + 1
    if n > 0:
        pos = pos + 1
    if n < 0:
        neg = neg + 1
print(f'{par} valor(es) par(es)')
print(f'{imp} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')
    
