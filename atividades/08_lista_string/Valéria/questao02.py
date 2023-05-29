qtd = 0

frase = input("Frase: ")

for s in frase:
    if (s == ' '):
        qtd += 1

print(qtd)
print(frase.count(" "))